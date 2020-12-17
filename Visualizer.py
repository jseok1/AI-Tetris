import pygame

import Tetris

FPS = 60

DIMENSIONS = (500, 600)
UNIT = 25

WIDTH = 10
HEIGHT = 20

WHITE = (255, 255, 255)
GREY = (240, 240, 240)

COLOURS = {'I': (90, 180, 255),
           'J': (50, 130, 245),
           'L': (255, 100, 35),
           'O': (255, 175, 5),
           'S': (15, 220, 25),
           'Z': (245, 55, 35),
           'T': (150, 100, 200)}

DELAY = 75 


class Visualizer:

    def __init__(self):
        self.game = None
        self.screen = None

    def run_game(self, level):
        """Initialize and run Tetris."""
        pygame.init()
        pygame.display.set_caption('Tetris')
        self.game = Tetris.Tetris(WIDTH, HEIGHT, level)
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
            clock.tick(FPS)
        pygame.quit()

    def draw(self):
        self.screen.fill((15, 45, 85))

        length = 25
        x_init = length
        y_init = length

        

        start = (110, 145, 200)
        end = (20, 55, 110)

        for x in range(length * WIDTH // 2):
            red = start[0] + (end[0] - start[0]) / (length * WIDTH) * x * 2
            green = start[1] + (end[1] - start[1]) / (length * WIDTH) * x * 2
            blue = start[2] + (end[2] - start[2]) / (length * WIDTH) * x * 2
            line = pygame.Rect(x_init + x, y_init, 1, length * HEIGHT)
            pygame.draw.rect(self.screen, (red, green, blue), line)

        for x in range(length * WIDTH // 2):
            red = end[0] + (start[0] - end[0]) / (length * WIDTH) * x * 2
            green = end[1] + (start[1] - end[1]) / (length * WIDTH) * x * 2
            blue = end[2] + (start[2] - end[2]) / (length * WIDTH) * x * 2
            line = pygame.Rect(x_init + x + length * WIDTH / 2, y_init, 1, length * HEIGHT)
            pygame.draw.rect(self.screen, (red, green, blue), line)

        self.draw_game_surface()
        self.draw_hold_surface()
        pygame.display.flip()

    def draw_hold_surface(self):
        surface = pygame.Surface((5 * UNIT, 2.5 * UNIT))
        # draw current tetromino
        tetromino = self.game.next_tetromino[0]
        for y in range(tetromino.length):
            for x in range(tetromino.length):
                if tetromino.shapes[tetromino.rotation][y][x] != '.':
                    block = pygame.Rect(x * UNIT, (y - 1) * UNIT, UNIT, UNIT)
                    colour = COLOURS[tetromino.shapes[tetromino.rotation][y][x]]
                    pygame.draw.rect(surface, colour, block)  

        self.screen.blit(surface, (12 * UNIT, UNIT))

    def draw_game_surface(self):
        """Render the current tetrominos and board."""
        surface = pygame.Surface((WIDTH * UNIT, HEIGHT * UNIT))

        # draw previous tetrominoes
        for y in range(HEIGHT):
            for x in range(WIDTH):
                if self.game.grid.grid[y + 1][x].isalpha():
                    block = pygame.Rect(x * UNIT, y * UNIT, UNIT, UNIT)
                    colour = COLOURS[self.game.grid.grid[y + 1][x]]
                    pygame.draw.rect(surface, colour, block)

        # draw current tetromino
        if self.game.game_state == 1:
            tetromino = self.game.current_tetromino
            for y in range(tetromino.length):
                for x in range(tetromino.length):
                    if tetromino.shapes[tetromino.rotation][y][x] != '.':
                        block = pygame.Rect((tetromino.x + x) * UNIT, (tetromino.y + y - 1) * UNIT, UNIT, UNIT)
                        colour = COLOURS[tetromino.shapes[tetromino.rotation][y][x]]
                        pygame.draw.rect(surface, colour, block)     
        
        self.screen.blit(surface, (UNIT, UNIT))
        
