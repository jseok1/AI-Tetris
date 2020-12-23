class Timer:

    def __init__(self, rate):
        self.count = 0
        self.rate = rate
    
    def tick(self):
        """Increment this timer by one frame."""
        self.count += 1
        if self.count == self.rate:
            self.count = 0
        return self.count

    def reset(self):
        """Reset this timer."""
        self.count = 0
