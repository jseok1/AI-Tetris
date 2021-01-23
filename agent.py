import pygame

from tetromino import Tetromino
from grid import Grid


class State:

    def __init__(self, x, y, orientation, predecessor):
        self.x = x
        self.y = y
        self.orientation = orientation
        self.predecessor = predecessor


class Agent:

    def __init__(self, weights):
        self.weights = weights
        self.stack = []

    def get_actions(self):
        """Return all possible actions."""
        return [lambda tetromino: tetromino.move(-1, 0),
                lambda tetromino: tetromino.move(1, 0),
                lambda tetromino: tetromino.move(0, 1),
                lambda tetromino: tetromino.rotate(-1),
                lambda tetromino: tetromino.rotate(1)]

    def get_states(self, tetromino, grid):
        """Return all possible states."""
        states = []
        visited = {(tetromino.x, tetromino.y, tetromino.orientation)}
        queue = [State(tetromino.x, tetromino.y, tetromino.orientation, None)]
        while len(queue) > 0:
            state = queue.pop(0)
            copy = Tetromino(tetromino.tetromino, state.x, state.y, state.orientation, tetromino.shapes)
            copy.move(0, 1)
            if not grid.can_place(copy):
                states.append(state)
            for action in self.get_actions():
                copy = Tetromino(tetromino.tetromino, state.x, state.y, state.orientation, tetromino.shapes)
                action(copy)
                if grid.can_place(copy) and (copy.x, copy.y, copy.orientation) not in visited:
                    visited.add((copy.x, copy.y, copy.orientation))
                    queue.append(State(copy.x, copy.y, copy.orientation, state))
        return states

    def evaluate(self, tetromino, grid, state):
        """Return the score for a given state."""
        features = [0] * 4
        copy = Grid(grid.width, grid.height - 2)
        copy.grid = [grid.grid[i][:] for i in range(grid.height)]
        copy.place_tetromino(Tetromino(tetromino.tetromino, state.x, state.y, state.orientation, tetromino.shapes))
        lines = copy.lines
        copy.update()
        features[0] = copy.lines - lines
        previous = 0
        for x in range(copy.width):
            current = 0
            for y in range(copy.height):
                if copy.grid[y][x] != 0 and current == 0:
                    current = copy.height - y
                    features[1] += current
                elif copy.grid[y][x] == 0 and current > 0:
                    features[3] += 1
            if x > 0:
                features[2] += abs(current - previous)
            previous = current
        score = 0
        for feature, weight in zip(features, self.weights):
            score += feature * weight
        return score

    def search(self, tetromino, grid):
        """Search for an optimal state."""
        optimal = (None, float('-inf'))
        for state in self.get_states(tetromino, grid):
            score = self.evaluate(tetromino, grid, state)
            if score > optimal[1]:
                optimal = (state, score)
        state = optimal[0]
        self.stack = [pygame.K_DOWN]  # manually place tetromino
        while state.predecessor is not None:
            adj_x = state.x - state.predecessor.x
            adj_y = state.y - state.predecessor.y
            adj_orientation = state.orientation - state.predecessor.orientation
            if adj_x == -1:
                self.stack.append(pygame.K_LEFT)
            elif adj_x == 1:
                self.stack.append(pygame.K_RIGHT)
            elif adj_y == 1:
                self.stack.append(pygame.K_DOWN)
            elif adj_orientation == -1 or adj_orientation == len(tetromino.shapes) - 1:
                self.stack.append(pygame.K_z)
            elif adj_orientation == 1 or adj_orientation == 1 - len(tetromino.shapes):
                self.stack.append(pygame.K_x)
            state = state.predecessor

    def play(self, tetromino, grid):
        """Return an optimal action."""
        if len(self.stack) == 0:
            self.search(tetromino, grid)
        return self.stack.pop()
