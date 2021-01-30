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
            actions = self.get_actions()
            for action in actions:
                copy = Tetromino(tetromino.tetromino, state.x, state.y, state.orientation, tetromino.shapes)
                action(copy)
                if grid.can_place(copy) and (copy.x, copy.y, copy.orientation) not in visited:
                    visited.add((copy.x, copy.y, copy.orientation))
                    queue.append(State(copy.x, copy.y, copy.orientation, state))
        return states

    def evaluate(self, tetromino, grid, state):
        """Return the optimality of a given state."""
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
        optimality = 0
        for feature, weight in zip(features, self.weights):
            optimality += feature * weight
        return optimality

    def play(self, tetromino, grid):
        """Find an optimal state and return an optimal action."""
        if len(self.stack) == 0:
            states = self.get_states(tetromino, grid)
            state = max(states, key=lambda state: self.evaluate(tetromino, grid, state))
            self.stack = [lambda game: game.move_down()]  # manually place tetromino
            while state.predecessor is not None:
                adj_x = state.x - state.predecessor.x
                adj_y = state.y - state.predecessor.y
                adj_orientation = state.orientation - state.predecessor.orientation
                if adj_x == -1:
                    self.stack.append(lambda game: game.move_left())
                elif adj_x == 1:
                    self.stack.append(lambda game: game.move_right())
                elif adj_y == 1:
                    self.stack.append(lambda game: game.move_down())
                elif adj_orientation == 1 or adj_orientation == 1 - len(tetromino.shapes):
                    self.stack.append(lambda game: game.rotate_clockwise())
                elif adj_orientation == -1 or adj_orientation == len(tetromino.shapes) - 1:
                    self.stack.append(lambda game: game.rotate_counterclockwise())
                state = state.predecessor
        return self.stack.pop()
