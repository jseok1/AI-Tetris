class Score:

    def __init__(self):
        self.score = 0

    def score_points(self, lines, level):
        if lines == 4:
            self.score += 1200 * level
        elif lines == 3:
            self.score += 300 * level
        elif lines == 2:
            self.score += 100 * level
        else:
            self.score += 40 * level
