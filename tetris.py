from grid import Grid
from randomizer import Randomizer
from score import Score
from timer import Timer


class Tetris:

    def __init__(self, width, height, level, gravity, seed):
        self.state = 1
        self.randomizer = Randomizer(seed)
        self.current_tetromino = self.randomizer.get_tetromino()
        self.next_tetromino = self.randomizer.get_tetromino()
        self.grid = Grid(width, height)
        self.score = Score()
        self.level = level
        self.gravity = gravity
        self.threshold = min(level * 10 + 10, max(100, level * 10 - 50))
        self.is_dropping = False
        self.delay = None
        self.timer = Timer(60)

    def move_left(self):
        """Move the current tetromino left, if possible."""
        self.current_tetromino.move(-1, 0)
        if not self.grid.can_place(self.current_tetromino):
            self.current_tetromino.move(1, 0)

    def move_right(self):
        """Move the current tetromino right, if possible."""
        self.current_tetromino.move(1, 0)
        if not self.grid.can_place(self.current_tetromino):
            self.current_tetromino.move(-1, 0)

    def move_down(self):
        """Move the current tetromino down, if possible."""
        self.current_tetromino.move(0, 1)
        if self.grid.can_place(self.current_tetromino):
            if self.is_dropping:
                self.score.points += 1
        else:
            self.current_tetromino.move(0, -1)
            self.grid.place_tetromino(self.current_tetromino)
            self.toggle_drop(False)
            if self.grid.can_clear():
                self.delay = Timer(20)
                self.state = 2
            else:
                self.delay = Timer(12)
                self.state = 3

    def toggle_drop(self, is_dropping):
        """Accelerate the speed of the current tetromino to 0.5G."""
        if is_dropping and not self.is_dropping:
            self.is_dropping = True
            self.accelerate_tetromino()
            self.move_down()
        elif not is_dropping and self.is_dropping:
            self.is_dropping = False
            self.accelerate_tetromino()

    def rotate_clockwise(self):
        """Rotate the current tetromino clockwise, if possible."""
        self.current_tetromino.rotate(1)
        if not self.grid.can_place(self.current_tetromino):
            self.current_tetromino.rotate(-1)

    def rotate_counterclockwise(self):
        """Rotate the current tetromino counterclockwise, if possible."""
        self.current_tetromino.rotate(-1)
        if not self.grid.can_place(self.current_tetromino):
            self.current_tetromino.rotate(1)
    
    def reset_tetromino(self):
        """Replace the current tetromino with another randomly generated tetromino."""
        self.timer.reset()
        self.current_tetromino = self.next_tetromino
        self.next_tetromino = self.randomizer.get_tetromino()
        return self.grid.can_place(self.current_tetromino)

    def accelerate_tetromino(self):
        """Accelerate the speed of the current tetromino."""
        if self.is_dropping:
            self.timer = Timer(min(2, self.timer.rate))
        else:
            if self.level < 9:
                self.timer = Timer(48 - self.level * 5)
            elif self.level == 9:
                self.timer = Timer(6)
            elif self.level > 9 and self.level < 13:
                self.timer = Timer(5)
            elif self.level > 12 and self.level < 16:
                self.timer = Timer(4)
            elif self.level > 15 and self.level < 19:
                self.timer = Timer(3)
            elif self.level > 18 and self.level < 29:
                self.timer = Timer(2)
            else:
                self.timer = Timer(1)

    def update(self):
        """Update this game."""
        if self.state == 1:  # running
            if self.gravity:
                if self.timer.tick() == 0:
                    if self.timer.rate > 48:
                        self.accelerate_tetromino()
                    self.move_down()
        elif self.state == 2:  # waiting for line clear
            count = self.delay.tick()
            if count == 0:
                lines = self.grid.lines
                self.grid.update()
                if self.grid.lines >= self.threshold:  
                    self.threshold += 10
                    self.level += 1
                    self.accelerate_tetromino()
                self.score.score(self.grid.lines - lines, self.level)
                self.delay = Timer(12)
                self.state = 3
            elif count > 1 and count < self.grid.width + 2:
                x = count - 2
                self.grid.clear(x)
        elif self.state == 3:  # waiting for next tetromino
            if self.delay.tick() == 0:
                if self.reset_tetromino():
                    self.state = 1
                else:
                    self.state = 0
