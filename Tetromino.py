class Tetromino:
    """A Tetromino class."""

    def __init__(self, states):
        """Initialize a new piece."""
        self.states = states
        self.x = 3
        self.y = -1
        self.rotation = 0

    def move(self, adj_x, adj_y):
        """Move this piece in the desired direction. """
        self.x += adj_x
        self.y += adj_y

    def rotate(self, direction):
        """Rotate this piece in the desired direction."""
        self.rotation = (self.rotation + direction) % len(self.states)
