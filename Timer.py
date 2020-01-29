class Timer:

    def __init__(self, rate):
        self.count = 0
        self.rate = rate
    
    def tick(self):
        self.count += 1
        if self.count == self.rate:
            self.count = 0
        return self.count
    
    def reset(self, rate):
        self.count = 0
        self.rate = rate
