class Score:

    def __init__(self):
        self.points = 0

    def score(self, lines, level):
        """Score points for the lines cleared on the given level."""
        if lines == 4:
            self.points += 1200 * (level + 1)
        elif lines == 3:
            self.points += 300 * (level + 1)
        elif lines == 2:
            self.points += 100 * (level + 1)
        else:
            self.points += 40 * (level + 1)
