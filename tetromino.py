class Tetromino:
  def __init__(self, type, x, y, orientation, shapes):
    self.type = type
    self.x = x
    self.y = y
    self.orientation = orientation
    self.shapes = shapes

  def move(self, delta_x, delta_y):
    """Move this Tetromino in a given direction."""
    self.x += delta_x
    self.y += delta_y

  def rotate(self, delta_orientation):
    """Rotate this Tetromino in a given direction."""
    self.orientation = (self.orientation + delta_orientation) % len(self.shapes)
