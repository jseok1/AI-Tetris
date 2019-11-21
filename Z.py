from Tetromino import Tetromino


class Z(Tetromino):
    """A Tetromino class for the 'Z' piece."""

    def __init__(self):
        """Initialize a new 'Z' piece."""
        states = [['.....',
                   '.ZZ..',
                   '..ZZ.',
                   '.....',
                   '.....'],
                  ['.....',
                   '...Z.',
                   '..ZZ.',
                   '..Z..',
                   '.....']]
        super().__init__(states)
