class Grid:

    def __init__(self, width, height):
        self.width = width
        self.height = height + 2
        self.grid = [[0] * self.width for _ in range(self.height)]
        self.lines = 0

    def can_place(self, tetromino):
        """Return true if a given tetromino can be placed on this grid. Return false otherwise."""
        for x, y in tetromino.shapes[tetromino.orientation]:
            if tetromino.x + x < 0 or tetromino.y + y < 0:
                return False    
            try:
                if self.grid[tetromino.y + y][tetromino.x + x] != 0:
                    return False
            except:
                return False
        return True

    def place_tetromino(self, tetromino):
        """Place a given tetromino on this grid."""
        for x, y in tetromino.shapes[tetromino.orientation]:
            self.grid[tetromino.y + y][tetromino.x + x] = tetromino.type

    def can_clear(self):
        """Return true if a completed line is on this grid. Return false otherwise."""
        for y in range(self.height):
            if 0 not in self.grid[y]:
                return True
        return False

    def clear(self, x):
        """Clear the completed lines on this grid."""
        for y in range(self.height):
            if 0 not in self.grid[y]:
                self.grid[y][x] = 9

    def update(self):
        """Update this grid."""
        for y in range(self.height):
            if 0 not in self.grid[y]:
                self.grid.remove(self.grid[y])
                self.grid.insert(0, [0] * self.width)
                self.lines += 1
