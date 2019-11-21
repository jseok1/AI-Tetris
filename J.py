from Tetromino import Tetromino


class J(Tetromino):
    """A Tetromino class for the 'J' piece."""

    def __init__(self):
        """Initialize a new 'J' piece."""
        states = [['.....',
                   '.J...',
                   '.JJJ.',
                   '.....',
                   '.....'],
                  ['.....',
                   '..JJ.',
                   '..J..',
                   '..J..',
                   '.....'],
                  ['.....',
                   '.....',
                   '.JJJ.',
                   '...J.',
                   '.....'],
                  ['.....',
                   '..J..',
                   '..J..',
                   '.JJ..',
                   '.....']]
        super().__init__(states)
