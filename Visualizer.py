import pygame

import Tetris

UNIT = 25
DIMENSIONS = (UNIT * 17, UNIT * 22)

WIDTH = 10
HEIGHT = 20

WHITE = (255, 255, 255)
LIGHT = (35, 65, 115)
DARK = (10, 20, 35)

COLOURS = {'I': (90, 180, 255),
           'J': (45, 120, 255),
           'L': (255, 100, 35),
           'O': (245, 180, 50),
           'S': (50, 225, 60),
           'Z': (245, 65, 45),
           'T': (185, 90, 235)}

FONT = 'Arial Narrow'


class Visualizer:

    def __init__(self, start):
        self.game = None
        self.start = start
        self.record = 0
        self.screen = None
        pygame.init()

    def run_game(self):
        """Initialize and run Tetris."""        
        pygame.display.set_caption('Tetris')
        self.game = Tetris.Tetris(WIDTH, HEIGHT, self.start)
        self.screen = pygame.display.set_mode(DIMENSIONS)
        self.game_loop()

    def game_loop(self):
        """Handle player input and draw to the screen."""
        clock = pygame.time.Clock()
        previous = None
        count = 0  # for delayed auto shift
        toggle = False  # for soft drop

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if self.game.game_state == 0:
                        if event.key == pygame.K_RETURN:
                            if self.game.score.score > self.record:
                                self.record = self.game.score.score
                            self.game = Tetris.Tetris(WIDTH, HEIGHT, self.start)
                    elif self.game.game_state == 1:
                        if event.key == pygame.K_SPACE:
                            self.game.hard_drop()
                        elif event.key == pygame.K_x:
                            self.game.rotate_clockwise()
                        elif event.key == pygame.K_z:
                            self.game.rotate_counterclockwise()

            keys = pygame.key.get_pressed()
            keys = {key: keys[key] for key in [pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]}
            pressed = sum(keys.values())      
            
            if (not keys[pygame.K_DOWN] or pressed > 1) and toggle:
                toggle = False
                self.game.soft_drop(toggle)

            if pressed < 2:
                current = -1
                for key in keys:
                    if keys[key]:
                        current = key
                        break

                if self.game.game_state == 1:
                    if current == pygame.K_DOWN:
                        if current != previous:
                            toggle = True
                            self.game.soft_drop(toggle)                            
                    elif current == pygame.K_LEFT or current == pygame.K_RIGHT:
                        if current != previous:
                            count = 0
                        blocked = False
                        if count % 15 == 0:
                            x = self.game.current_tetromino.x
                            if current == pygame.K_LEFT:
                                self.game.move_left()
                            else:
                                self.game.move_right()
                            if self.game.current_tetromino.x == x:
                                blocked = True
                        if blocked:
                            count = 15
                        elif count == 15:
                            count = 10
                        else:
                            count += 1
                previous = current

            self.game.update()
            self.draw()
            clock.tick(60)

    def draw(self):
        rate = ((DARK[0] - LIGHT[0]) / DIMENSIONS[1],
                (DARK[1] - LIGHT[1]) / DIMENSIONS[1],
                (DARK[2] - LIGHT[2]) / DIMENSIONS[1])

        for i in range(DIMENSIONS[1]):
            colour = (min(max(LIGHT[0] + rate[0] * i, 0), 255),
                      min(max(LIGHT[1] + rate[1] * i, 0), 255),
                      min(max(LIGHT[2] + rate[2] * i, 0), 255))
            line = pygame.Rect(0, i, DIMENSIONS[0], 1)
            pygame.draw.rect(self.screen, colour, line)

        self.render_text('HIGH SCORE', 26, (UNIT * 12, UNIT * 9))
        self.render_text(f'{self.record}', 40, (UNIT * 12, UNIT * 10))

        self.render_text('SCORE', 26, (UNIT * 12, UNIT * 12))
        self.render_text(f'{self.game.score.score}', 40, (UNIT * 12, UNIT * 13))

        self.render_text('LEVEL', 26, (UNIT * 12, UNIT * 15))
        self.render_text(f'{self.game.level}', 40, (UNIT * 12, UNIT * 16))

        self.render_text('LINES', 26, (UNIT * 12, UNIT * 18))
        self.render_text(f'{self.game.lines}', 40, (UNIT * 12, UNIT * 19))

        self.draw_game_surface()
        self.draw_hold_surface()
        pygame.display.flip()

    def render_text(self, text, size, position):
        font = pygame.font.SysFont(FONT, size)
        surface = font.render(text, True, WHITE)
        self.screen.blit(surface, position)


    def draw_hold_surface(self):
        # generalize to many pieces
        surface = pygame.Surface((5 * UNIT, 2 * UNIT), pygame.SRCALPHA)
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
        surface = pygame.Surface((WIDTH * UNIT + 2, HEIGHT * UNIT + 1), pygame.SRCALPHA)

        # draw border
        line = pygame.Rect(0, 0, 1, UNIT * HEIGHT)
        pygame.draw.rect(surface, WHITE, line)

        line = pygame.Rect(UNIT * WIDTH + 1, 0, 1, UNIT * HEIGHT)
        pygame.draw.rect(surface, WHITE, line)

        line = pygame.Rect(0, UNIT * HEIGHT, UNIT * WIDTH + 2, 1)
        pygame.draw.rect(surface, WHITE, line)

        # draw previous tetrominoes
        for y in range(HEIGHT):
            for x in range(WIDTH):
                if self.game.grid.grid[y + 2][x].isalpha():
                    block = pygame.Rect(x * UNIT + 1, y * UNIT, UNIT, UNIT)
                    colour = COLOURS[self.game.grid.grid[y + 2][x]]
                    pygame.draw.rect(surface, colour, block)

        # draw current tetromino
        if self.game.game_state == 1:
            tetromino = self.game.current_tetromino
            for y in range(tetromino.length):
                for x in range(tetromino.length):
                    if tetromino.shapes[tetromino.rotation][y][x] != '.':
                        block = pygame.Rect((tetromino.x + x) * UNIT + 1, (tetromino.y + y - 2) * UNIT, UNIT, UNIT)
                        colour = COLOURS[tetromino.shapes[tetromino.rotation][y][x]]
                        pygame.draw.rect(surface, colour, block)     
        
        self.screen.blit(surface, (UNIT, UNIT))
        
