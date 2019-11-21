import pygame

from Tetris import Tetris

# screen dimensions
WIDTH = 340
HEIGHT = 680

# RGB colour values
WHITE = (255, 255, 255)
GREY = (240, 240, 240)

CYAN = (130, 215, 255)
BLUE = (100, 170, 255)
ORANGE = (255, 170, 70)
YELLOW = (255, 220, 100)
GREEN = (155, 255, 110)
RED = (255, 100, 100)
PURPLE = (170, 140, 255)


def run_visualizer():
    """Initialize and run this visualizer."""
    pygame.init()
    pygame.display.set_caption('Tetris')
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    game = Tetris()

    event_loop(screen, game)


def event_loop(screen, game):
    """Respond to events and update the visualizer."""
    falling_piece_event = pygame.USEREVENT + 1
    pygame.time.set_timer(falling_piece_event, 800)
    # pygame.key.set_repeat(100, 100)
    is_running = True
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    game.move_left()
                elif event.key == pygame.K_RIGHT:
                    game.move_right()
                elif event.key == pygame.K_DOWN:
                    game.move_down()
                elif event.key == pygame.K_SPACE:
                    game.drop_down()
                elif event.key == pygame.K_x:
                    game.rotate_clockwise()
                elif event.key == pygame.K_z:
                    game.rotate_counterclockwise()
            elif event.type == falling_piece_event:
                game.move_down()
                if game.game_is_over:
                    is_running = False
            draw(screen, game)
            pygame.display.flip()


def draw(screen, game):
    screen.fill(WHITE)  # clear screen
    width = WIDTH / 10
    height = HEIGHT / 20

    for y in range(20):
        line = pygame.Rect(0, y * height, WIDTH, 1)
        pygame.draw.rect(screen, GREY, line)
    for x in range(10):
        line = pygame.Rect(x * width, 0, 1, HEIGHT)
        pygame.draw.rect(screen, GREY, line)

    for y in range(20):
        for x in range(10):
            block = pygame.Rect(x * width, y * height, width, height)
            if game.board.board[y][x] == 'I':
                pygame.draw.rect(screen, CYAN, block)
            elif game.board.board[y][x] == 'J':
                pygame.draw.rect(screen, BLUE, block)
            elif game.board.board[y][x] == 'L':
                pygame.draw.rect(screen, ORANGE, block)
            elif game.board.board[y][x] == 'O':
                pygame.draw.rect(screen, YELLOW, block)
            elif game.board.board[y][x] == 'S':
                pygame.draw.rect(screen, GREEN, block)
            elif game.board.board[y][x] == 'Z':
                pygame.draw.rect(screen, RED, block)
            elif game.board.board[y][x] == 'T':
                pygame.draw.rect(screen, PURPLE, block)


if __name__ == '__main__':
    run_visualizer()
