import pygame
import json

from tetris import Tetris
from agent import Agent
from timer import Timer

UNIT = 25
DIMENSIONS = (UNIT * 17, UNIT * 22)
BLOCK = (UNIT, UNIT)

WIDTH = 10
HEIGHT = 20

WHITE = (255, 255, 255)
LIGHT = (35, 65, 115)
DARK = (10, 20, 35)

COLOURS = [(90, 180, 255),
           (45, 120, 255),
           (255, 100, 35),
           (245, 180, 50),
           (50, 225, 60),
           (245, 65, 45),
           (185, 90, 235)]

FONT = 'Arial Narrow'

WEIGHTS = [0.783709568447, -0.89886513238, -0.288592282201, -0.4428466993816]


class Visualizer:

    def __init__(self, mode, level):
        pygame.init()
        self.mode = mode
        self.level = level
        self.game = Tetris(WIDTH, HEIGHT, self.level, self.mode == 1, None)
        self.screen = pygame.display.set_mode(DIMENSIONS)
        self.record = 0
        self.pressed = pygame.key.get_pressed()
        self.count = 0
        self.paused = False
        self.agent = None
        self.timer = Timer(1)
        if self.mode == 0:
            self.agent = Agent(WEIGHTS)            
        elif self.mode == 1:
            try:
                with open('data.json', 'r') as f:
                    self.record = json.load(f)['record']
            except:
                pass
        pygame.display.set_caption('Tetris')
        self.run()

    def run(self):
        """Run this game."""
        clock = pygame.time.Clock()
        count = 0
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    if self.mode == 1:
                        with open('data.json', 'w') as f:
                            json.dump({'record': self.record}, f)
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if self.game.state == 0:
                            if self.game.score.points > self.record and self.mode == 1:
                                self.record = self.game.score.points
                            self.game = Tetris(WIDTH, HEIGHT, self.level, self.mode == 1, None)
                        else:
                            self.paused = not self.paused
            pressed = pygame.key.get_pressed()
            if not self.paused:
                if self.game.state == 1:
                    if self.mode == 0:
                        if self.timer.tick() == 0:
                            self.agent.play(self.game.current_tetromino, self.game.grid)(self.game)
                    elif self.mode == 1:
                        self.interact(pressed)
                self.game.update()
            self.pressed = pressed
            self.render()
            clock.tick(60)

    def interact(self, pressed):
        """Handle player input."""
        if pressed[pygame.K_x] and not self.pressed[pygame.K_x]:
            self.game.rotate_clockwise()
        elif pressed[pygame.K_z] and not self.pressed[pygame.K_z]:
            self.game.rotate_counterclockwise()
        count = 0
        if pressed[pygame.K_LEFT]:
            count += 1
        if pressed[pygame.K_RIGHT]:
            count += 1
        if pressed[pygame.K_DOWN]:
            count += 1
        if not pressed[pygame.K_DOWN] or count > 1:
            self.game.toggle_drop(False)
        if count == 1:
            if pressed[pygame.K_LEFT] or pressed[pygame.K_RIGHT]:
                x = self.game.current_tetromino.x
                if pressed[pygame.K_LEFT]:
                    if not self.pressed[pygame.K_LEFT]:
                        self.count = 0
                    if self.count % 15 == 0:
                        self.game.move_left()
                elif pressed[pygame.K_RIGHT]:
                    if not self.pressed[pygame.K_RIGHT]:
                        self.count = 0
                    if self.count % 15 == 0:
                        self.game.move_right()
                if self.count % 15 == 0 and self.game.current_tetromino.x == x:
                    self.count = 15
                elif self.count == 15:
                    self.count = 10
                else:
                    self.count += 1
            elif pressed[pygame.K_DOWN]:
                self.game.toggle_drop(True)

    def render(self):
        """Render this game."""
        rate = ((DARK[0] - LIGHT[0]) / DIMENSIONS[1],
                (DARK[1] - LIGHT[1]) / DIMENSIONS[1],
                (DARK[2] - LIGHT[2]) / DIMENSIONS[1])

        for i in range(DIMENSIONS[1]):
            colour = (min(max(LIGHT[0] + rate[0] * i, 0), 255),
                      min(max(LIGHT[1] + rate[1] * i, 0), 255),
                      min(max(LIGHT[2] + rate[2] * i, 0), 255))
            pygame.draw.line(self.screen, colour, (0, i), (DIMENSIONS[0], i))
    
        pygame.draw.line(self.screen, WHITE, (UNIT, UNIT), (UNIT, UNIT * (HEIGHT + 1)))
        pygame.draw.line(self.screen, WHITE, (UNIT * (WIDTH + 1) + 1, UNIT), (UNIT * (WIDTH + 1) + 1, UNIT * (HEIGHT + 1)))
        pygame.draw.line(self.screen, WHITE, (UNIT, UNIT * (HEIGHT + 1)), (UNIT * (WIDTH + 1) + 1, UNIT * (HEIGHT + 1)))

        header = pygame.font.SysFont(FONT, 26)
        body = pygame.font.SysFont(FONT, 40)
        self.screen.blit(header.render('HIGH SCORE', True, WHITE), (UNIT * 12, UNIT * 9))
        self.screen.blit(body.render(f'{self.record}', True, WHITE), (UNIT * 12, UNIT * 10))
        self.screen.blit(header.render('SCORE', True, WHITE), (UNIT * 12, UNIT * 12))
        self.screen.blit(body.render(f'{self.game.score.points}', True, WHITE), (UNIT * 12, UNIT * 13))
        self.screen.blit(header.render('LEVEL', True, WHITE), (UNIT * 12, UNIT * 15))
        self.screen.blit(body.render(f'{self.game.level}', True, WHITE), (UNIT * 12, UNIT * 16))
        self.screen.blit(header.render('LINES', True, WHITE), (UNIT * 12, UNIT * 18))
        self.screen.blit(body.render(f'{self.game.grid.lines}', True, WHITE), (UNIT * 12, UNIT * 19))

        if self.game.state == 1:
            for x, y in self.game.current_tetromino.shapes[self.game.current_tetromino.orientation]:
                coordinates = ((self.game.current_tetromino.x + x + 1) * UNIT + 1, (self.game.current_tetromino.y + y - 1) * UNIT)
                block = pygame.Rect(coordinates, BLOCK)
                colour = COLOURS[self.game.current_tetromino.tetromino - 1]
                pygame.draw.rect(self.screen, colour, block)

        for x, y in self.game.next_tetromino.shapes[self.game.next_tetromino.orientation]:
            coordinates = ((x + 14) * UNIT, (y + 1) * UNIT)
            block = pygame.Rect(coordinates, BLOCK)
            colour = COLOURS[self.game.next_tetromino.tetromino - 1]
            pygame.draw.rect(self.screen, colour, block)
        
        for y in range(2, HEIGHT + 2):
            for x in range(WIDTH):
                if self.game.grid.grid[y][x] != 0 and self.game.grid.grid[y][x] != 9:
                    coordinates = ((x + 1) * UNIT + 1, (y - 1) * UNIT)
                    block = pygame.Rect(coordinates, BLOCK)
                    colour = COLOURS[self.game.grid.grid[y][x] - 1]
                    pygame.draw.rect(self.screen, colour, block)

        pygame.display.flip()
