class Board:
    """A board class."""

    def __init__(self, width, height):
        """Initialize a new board."""
        self.board = [['.' for x in range(width)] for y in range(height)]
        self.width = width
        self.height = height

    def is_full(self, n):
        """Returns True if row n is full, False otherwise."""
        for x in range(self.width):
            if self.board[n][x] == '.':
                return False
        return True

    def clear_line(self, n):
        for y in range(n, 0, -1):
            self.board[y] = self.board[y - 1].copy()
        self.board[0] = ['.' for x in range(self.width)]

    def clear_lines(self):
        for y in range(self.height):
            if self.is_full(y):
                self.clear_line(y)

    def add_piece(self, piece):
        for y in range(len(piece.states[0])):
            for x in range(len(piece.states[0][0])):
                if piece.states[piece.rotation][y][x] != '.':
                    self.board[piece.y + y][piece.x + x] = piece.states[piece.rotation][y][x]

    def remove_piece(self, piece):
        for y in range(len(piece.states[0])):
            for x in range(len(piece.states[0][0])):
                if piece.states[piece.rotation][y][x] != '.':
                    self.board[piece.y + y][piece.x + x] = '.'

    def can_move(self, piece, adj_x, adj_y):
        for y in range(len(piece.states[0])):
            for x in range(len(piece.states[0][0])):
                if piece.states[piece.rotation][y][x] != '.':
                    x_new = piece.x + x + adj_x   # coordinates on board
                    y_new = piece.y + y + adj_y
                    if x_new < 0 or x_new > self.width - 1:
                        return False
                    if y_new < 0 or y_new > self.height - 1:
                        return False
                    if self.board[y_new][x_new] != '.':
                        return False
        return True

    def can_rotate(self, piece, direction):
        for y in range(len(piece.states[0])):
            for x in range(len(piece.states[0][0])):
                if piece.states[(piece.rotation + direction) % len(piece.states)][y][x] != '.':
                    if piece.x + x < 0 or piece.x + x > self.width - 1:
                        return False
                    if piece.y + y < 0 or piece.y + y > self.height - 1:
                        return False
                    if self.board[piece.y + y][piece.x + x] != '.':
                        return False
        return True
