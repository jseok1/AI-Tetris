from Tetromino import Tetromino


class L(Tetromino):
    """A Tetromino class for the 'L' piece."""

    def __init__(self):
        """Initialize a new 'L' piece."""
        states = [['.....',
                   '...L.',
                   '.LLL.',
                   '.....',
                   '.....'],
                  ['.....',
                   '..L..',
                   '..L..',
                   '..LL.',
                   '.....'],
                  ['.....',
                   '.....',
                   '.LLL.',
                   '.L...',
                   '.....'],
                  ['.....',
                   '.LL..',
                   '..L..',
                   '..L..',
                   '.....']]
        super().__init__(states)
