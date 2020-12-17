class Timer:

    def __init__(self, frames):
        self.count = 0
        self.frames = frames
    
    def tick(self):
        self.count += 1
        if self.count == self.frames:
            self.count = 0
        return self.count

    def reset(self):
        self.count = 0
