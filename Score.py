class Score:

    def __init__(self):
        self.score = 0

    def score_points(self, lines_cleared):
        if lines_cleared == 4:
            self.score += 800
        elif lines_cleared == 3:
            self.score += 500
        else:
            self.score += lines_cleared * 100
