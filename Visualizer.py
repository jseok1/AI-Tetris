import pygame

DIMENSIONS = (300, 600)
FPS = 60

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


class Visualizer:

    def __init__(self, game):
        self.game = game

    def run_game(self):
        """Initialize and run this visualizer."""
        pygame.init()
        pygame.display.set_caption('Tetris')
        screen = pygame.display.set_mode(DIMENSIONS)
        self.game_loop(screen)

    def game_loop(self, screen):
        """Respond to events and update the visualizer."""
        clock = pygame.time.Clock()
        is_running = True
        while is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_running = False
                elif event.type == pygame.KEYDOWN:
                    if self.game.game_state == 1:
                        if event.key == pygame.K_LEFT:
                            self.game.move_left()
                        elif event.key == pygame.K_RIGHT:
                            self.game.move_right()
                        elif event.key == pygame.K_DOWN:
                            self.game.move_down()
                        if event.key == pygame.K_SPACE:
                            self.game.drop_down()
                        elif event.key == pygame.K_x:
                            self.game.rotate_clockwise()
                        elif event.key == pygame.K_z:
                            self.game.rotate_counterclockwise()
            self.game.update()
            self.draw(screen)
            if self.game.game_state == 0:
                is_running = False
            clock.tick(FPS)
        pygame.quit()

    def draw(self, screen):
        screen.fill(WHITE)
        width = DIMENSIONS[0] / 10
        height = DIMENSIONS[1] / 20

        for y in range(20):
            line = pygame.Rect(0, y * height, DIMENSIONS[0], 1)
            pygame.draw.rect(screen, GREY, line)
        for x in range(10):
            line = pygame.Rect(x * width, 0, 1, DIMENSIONS[1])
            pygame.draw.rect(screen, GREY, line)

        for y in range(20):
            for x in range(10):
                if self.game.grid.grid[y][x].isupper():
                    block = pygame.Rect(x * width, y * height, width, height)
                    colour = COLOURS[self.game.grid.grid[y][x]]
                    pygame.draw.rect(screen, colour, block)

        if self.game.game_state == 1:
            for y in range(4):
                for x in range(4):
                    if self.game.current_tetromino.shapes[self.game.current_tetromino.rotation][y][x] != '.':
                        block = pygame.Rect((self.game.current_tetromino.x + x) * width, (self.game.current_tetromino.y + y) * height, width, height)
                        colour = COLOURS[self.game.current_tetromino.shapes[self.game.current_tetromino.rotation][y][x]]
                        pygame.draw.rect(screen, colour, block)
        pygame.display.flip()
