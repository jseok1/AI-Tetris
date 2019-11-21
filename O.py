from Tetromino import Tetromino


class O(Tetromino):
    """A Tetromino class for the 'O' piece."""

    def __init__(self):
        """Initialize a new 'O' piece."""
        states = [['.....',
                   '..OO.',
                   '..OO.',
                   '.....',
                   '.....']]
        super().__init__(states)
