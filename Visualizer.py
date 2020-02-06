import pygame

import Tetris

DIMENSIONS = (600, 800)  # 3:4 aspect ratio recommended
FPS = 60

WIDTH = 10
HEIGHT = 20

WHITE = (255, 255, 255)
GREY = (240, 240, 240)

COLOURS = {'I': (130, 215, 255),
           'J': (100, 170, 255),
           'L': (255, 170, 70),
           'O': (255, 220, 100),
           'S': (155, 255, 110),
           'Z': (255, 100, 100),
           'T': (170, 140, 255),
           'X': (209, 243, 255)}

DELAY = 75 


class Visualizer:

    def __init__(self):
        self.game = None
        self.screen = None

    def run_game(self):
        """Initialize and run Tetris."""
        pygame.init()
        pygame.display.set_caption('Tetris')
        self.game = Tetris.Tetris(WIDTH, HEIGHT)
        self.screen = pygame.display.set_mode(DIMENSIONS)
        self.game_loop()

    def game_loop(self):
        """Handle player input and draw to the screen."""
        clock = pygame.time.Clock()
        prev_time = pygame.time.get_ticks()
        is_running = True

        while is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_running = False
                elif event.type == pygame.KEYDOWN and self.game.game_state == 1:
                    if event.key == pygame.K_SPACE:
                        self.game.drop_down()
                    elif event.key == pygame.K_x:
                        self.game.rotate_clockwise()
                    elif event.key == pygame.K_z:
                        self.game.rotate_counterclockwise()

            pressed = pygame.key.get_pressed()
            curr_time = pygame.time.get_ticks()
            if curr_time > prev_time + DELAY and self.game.game_state == 1:
                if pressed[pygame.K_LEFT]:
                    self.game.move_left()
                elif pressed[pygame.K_RIGHT]:
                    self.game.move_right()
                elif pressed[pygame.K_DOWN]:
                    self.game.move_down()
                prev_time = pygame.time.get_ticks()
                

                
            self.game.update()
            self.draw()
            if self.game.game_state == 0:
                is_running = False
            clock.tick(FPS)
        pygame.quit()

    def draw(self):
        self.screen.fill(WHITE)

        length = DIMENSIONS[1] * 0.9 / HEIGHT
        x_init = (DIMENSIONS[0] - length * 15) / 2
        y_init = length

        for y in range(HEIGHT + 1):
            line = pygame.Rect(x_init, y_init + y * length, length * WIDTH, 1)
            pygame.draw.rect(self.screen, GREY, line)
        for x in range(WIDTH + 1):
            line = pygame.Rect(x_init + x * length, y_init, 1, length * HEIGHT)
            pygame.draw.rect(self.screen, GREY, line)

        for y in range(HEIGHT):
            for x in range(WIDTH):
                if self.game.grid.grid[y][x].isalpha():
                    block = pygame.Rect(x_init + x * length, y_init + y * length, length, length)
                    colour = COLOURS[self.game.grid.grid[y][x]]
                    pygame.draw.rect(self.screen, colour, block)

        if self.game.game_state == 1:
            tetromino = self.game.current_tetromino
            for y in range(tetromino.length):
                for x in range(tetromino.length):
                    if tetromino.shapes[tetromino.rotation][y][x] != '.':
                        block = pygame.Rect(x_init + (tetromino.x + x) * length, y_init + (tetromino.y + y) * length, length, length)
                        colour = COLOURS[tetromino.shapes[tetromino.rotation][y][x]]
                        pygame.draw.rect(self.screen, colour, block)


        
        pygame.display.flip()





    
