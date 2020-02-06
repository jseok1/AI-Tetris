class Tetromino:
    """A Tetromino class."""

    def __init__(self, x, y, rotation, shapes, length):
        """Initialize a new Tetromino."""
        self.x = x
        self.y = y
        self.rotation = rotation
        self.shapes = shapes
        self.length = length

    def move(self, adj_x, adj_y):
        """Move this Tetromino in the desired direction."""
        self.x += adj_x
        self.y += adj_y

    def rotate(self, adj_rot):
        """Rotate this Tetromino in the desired direction."""
        self.rotation = (self.rotation + adj_rot) % len(self.shapes)
