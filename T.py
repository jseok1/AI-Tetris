from Tetromino import Tetromino


class T(Tetromino):
    """A Tetromino class for the 'T' piece."""

    def __init__(self):
        """Initialize a new 'T' piece."""
        states = [['.....',
                   '..T..',
                   '.TTT.',
                   '.....',
                   '.....'],
                  ['.....',
                   '..T..',
                   '..TT.',
                   '..T..',
                   '.....'],
                  ['.....',
                   '.....',
                   '.TTT.',
                   '..T..',
                   '.....'],
                  ['.....',
                   '..T..',
                   '.TT..',
                   '..T..',
                   '.....']]
        super().__init__(states)
