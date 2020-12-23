import Grid
import Randomizer
import Score
import Tetromino
import Timer


class Tetris:

    def __init__(self, width, height, level):
        self.game_state = 1
        self.randomizer = Randomizer.Randomizer()
        self.current_tetromino = self.randomizer.get_tetromino()
        self.next_tetromino = [self.randomizer.get_tetromino()]
        self.hold_tetromino = None  # unused for now
        self.grid = Grid.Grid(width, height)
        self.level = level
        self.score = Score.Score()
        self.lines = 0
        self.threshold = min(level * 10 + 10, max(100, level * 10 - 50))
        self.delay = None
        self.timer = None
        self.accelerate_tetromino()

    def move_left(self):
        """Move the current tetromino left, if possible."""
        if self.grid.can_place(self.current_tetromino, -1, 0, 0):
            self.current_tetromino.move(-1, 0)

    def move_right(self):
        """Move the current tetromino right, if possible."""
        if self.grid.can_place(self.current_tetromino, 1, 0, 0):
            self.current_tetromino.move(1, 0)

    def move_down(self):
        """Move the current tetromino down, if possible."""
        if self.grid.can_place(self.current_tetromino, 0, 1, 0):
            self.current_tetromino.move(0, 1)
        else:
            self.place_tetromino()

    def soft_drop(self, toggle):
        """Accelerate the speed of the current tetromino to 0.5G."""
        if toggle:
            self.timer = Timer.Timer(2)
        else:
            self.accelerate_tetromino()

    def hard_drop(self):
        """Accelerate the speed of the current tetromino to 20G."""
        while self.grid.can_place(self.current_tetromino, 0, 1, 0):
            self.current_tetromino.move(0, 1)
        self.place_tetromino()

    def rotate_clockwise(self):
        """Rotate the current tetromino clockwise, if possible."""
        if self.grid.can_place(self.current_tetromino, 0, 0, 1):
            self.current_tetromino.rotate(1)

    def rotate_counterclockwise(self):
        """Rotate the current tetromino counterclockwise, if possible."""
        if self.grid.can_place(self.current_tetromino, 0, 0, -1):
            self.current_tetromino.rotate(-1)
    
    def place_tetromino(self):
        """Place the current tetromino in its current position."""
        self.grid.place_tetromino(self.current_tetromino)
        if self.grid.can_clear():
            self.delay = Timer.Timer(20)
            self.game_state = 2
        else:
            self.timer.reset()
            self.delay = Timer.Timer(10)
            self.game_state = 3

    def reset_tetromino(self):
        """Replace the current tetromino with another randomly generated tetromino."""
        self.current_tetromino = self.next_tetromino.pop(0)
        self.next_tetromino.append(self.randomizer.get_tetromino())
        if not self.grid.can_place(self.current_tetromino, 0, 0, 0):
            self.game_state = 0

    def accelerate_tetromino(self):
        """Accelerate the speed of the current tetromino."""
        if self.level < 9:
            self.timer = Timer.Timer(48 - self.level * 5)
        elif self.level == 9:
            self.timer = Timer.Timer(6)
        elif self.level > 9 and self.level < 13:
            self.timer = Timer.Timer(5)
        elif self.level > 12 and self.level < 16:
            self.timer = Timer.Timer(4)
        elif self.level > 15 and self.level < 19:
            self.timer = Timer.Timer(3)
        elif self.level > 18 and self.level < 29:
            self.timer = Timer.Timer(2)
        else:
            self.timer = Timer.Timer(1)

    def update(self):
        """Update the game at every frame."""
        if self.game_state == 1:  # running
            if self.timer.tick() == 0:  
                self.move_down()
        elif self.game_state == 2:  # clearing lines
            count = self.delay.tick()
            if count == 0:
                lines = self.grid.shift_lines()
                self.lines += lines
                if self.lines >= self.threshold:  
                    self.threshold += 10  # accelerate every 10 lines after first acceleration
                    self.level += 1
                    self.accelerate_tetromino()
                self.timer.reset()
                self.score.score_points(lines, self.level)
                self.delay = Timer.Timer(10)
                self.game_state = 3
            elif count > 1:
                self.grid.clear_lines()
        elif self.game_state == 3:  # waiting for next tetromino
            if self.delay.tick() == 0:
                self.game_state = 1
                self.reset_tetromino()
