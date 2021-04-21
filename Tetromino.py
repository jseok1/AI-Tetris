class Tetromino:

    def __init__(self, type, x, y, orientation, shapes):
        self.type = type
        self.x = x
        self.y = y
        self.orientation = orientation
        self.shapes = shapes

    def move(self, adj_x, adj_y):
        """Move this tetromino in a given direction."""
        self.x += adj_x
        self.y += adj_y

    def rotate(self, adj_orientation):
        """Rotate this tetromino in a given direction."""
        self.orientation = (self.orientation + adj_orientation) % len(self.shapes)
