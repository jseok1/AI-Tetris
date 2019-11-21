from Tetromino import Tetromino


class S(Tetromino):
    """A Tetromino class for the 'S' piece."""

    def __init__(self):
        """Initialize a new 'S' piece."""
        states = [['.....',
                   '..SS.',
                   '.SS..',
                   '.....',
                   '.....'],
                  ['.....',
                   '.S...',
                   '.SS..',
                   '..S..',
                   '.....']]
        super().__init__(states)
