from Tetromino import Tetromino


class I(Tetromino):
    """A Tetromino class for the 'I' piece."""

    def __init__(self):
        """Initialize a new 'I' piece."""
        states = [['.....',
                   '.....',
                   'IIII.',
                   '.....',
                   '.....'],
                  ['..I..',
                   '..I..',
                   '..I..',
                   '..I..',
                   '.....']]
        super().__init__(states)
