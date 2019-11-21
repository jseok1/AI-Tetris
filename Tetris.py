import Board
import Randomizer

WIDTH = 10
HEIGHT = 20


class Tetris:

    def __init__(self):
        self.board = Board.Board(WIDTH, HEIGHT)
        self.randomizer = Randomizer.Randomizer()
        self.falling_tetromino = self.randomizer.get_tetromino()
        self.game_is_over = False

    def try_move(self, adj_x, adj_y):
        self.board.remove_piece(self.falling_tetromino)
        if self.board.can_move(self.falling_tetromino, adj_x, adj_y):
            self.falling_tetromino.move(adj_x, adj_y)
            self.board.add_piece(self.falling_tetromino)
            return True
        self.board.add_piece(self.falling_tetromino)
        return False

    def move_left(self):
        self.try_move(-1, 0)

    def move_right(self):
        self.try_move(1, 0)

    def move_down(self):
        if not self.try_move(0, 1):
            self.reset()

    def drop_down(self):
        is_falling = True
        while is_falling:
            is_falling = self.try_move(0, 1)
        self.reset()

    def try_rotate(self, direction):
        self.board.remove_piece(self.falling_tetromino)
        if self.board.can_rotate(self.falling_tetromino, direction):
            self.falling_tetromino.rotate(direction)
        self.board.add_piece(self.falling_tetromino)

    def rotate_clockwise(self):
        self.try_rotate(1)

    def rotate_counterclockwise(self):
        self.try_rotate(-1)

    def reset(self):
        self.board.clear_lines()
        self.falling_tetromino = self.randomizer.get_tetromino()
        if self.board.can_move(self.falling_tetromino, 0, 0):
            self.board.add_piece(self.falling_tetromino)
        else:
            self.game_is_over = True
