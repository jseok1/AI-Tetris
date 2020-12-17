class Grid:
    """A grid implementation."""

    def __init__(self, width, height):
        """Initialize a new grid with width <width> and height <height>."""
        self.width = width
        self.height = height + 1
        self.grid = [['.'] * self.width for _ in range(self.height)]

    def can_clear(self):
        """Return true if and only if a line can be cleared."""
        for y in range(self.height):
            if '.' not in self.grid[y]:
                return True
        return False

    def clear_line(self, n):
        """Clear the next non-empty block in line <n>, from left to right."""
        if self.grid[n][0] != '-':
            self.grid[n][0] = '-'
        else:
            for x in range(self.width - 2, -1, -1):
                if self.grid[n][x] == '-':
                    self.grid[n][x + 1] = '-'
                    break

    def clear_lines(self):
        for y in range(self.height):
            if '.' not in self.grid[y]:
                self.clear_line(y)
                
    def shift_line(self, n):
        for y in range(n, 0, -1):
            self.grid[y] = self.grid[y - 1].copy()
        self.grid[0] = ['.'] * self.width

    def shift_lines(self):
        lines = 0
        for y in range(self.height):
            if '.' not in self.grid[y]:
                self.shift_line(y)
                lines += 1
        return lines

    def can_place(self, tetromino, adj_x, adj_y, adj_rot):
        """Return true if and only if <tetromino> can be placed."""
        for y in range(tetromino.length):
            for x in range(tetromino.length):
                new_rot = (tetromino.rotation + adj_rot) % len(tetromino.shapes)
                if tetromino.shapes[new_rot][y][x] != '.':
                    new_x = tetromino.x + x + adj_x
                    new_y = tetromino.y + y + adj_y
                    if new_x < 0 or new_x > self.width - 1:
                        return False
                    if new_y < 0 or new_y > self.height - 1:
                        return False
                    if self.grid[new_y][new_x] != '.':
                        return False
        return True

    def place_tetromino(self, tetromino):
        for y in range(tetromino.length):
            for x in range(tetromino.length):
                block = tetromino.shapes[tetromino.rotation][y][x]
                if block != '.':
                    self.grid[tetromino.y + y][tetromino.x + x] = block
