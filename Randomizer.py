from random import shuffle

from I import I
from J import J
from L import L
from O import O
from S import S
from T import T
from Z import Z


class Randomizer:

    def __init__(self):
        self.bag = []

    def get_tetromino(self):
        if len(self.bag) == 0:
            self.bag = ['I', 'J', 'L', 'O', 'S', 'Z', 'T']
            shuffle(self.bag)
        tetromino = self.bag.pop()
        if tetromino == 'I':
            return I()
        elif tetromino == 'J':
            return J()
        elif tetromino == 'L':
            return L()
        elif tetromino == 'O':
            return O()
        elif tetromino == 'S':
            return S()
        elif tetromino == 'Z':
            return Z()
        elif tetromino == 'T':
            return T()
        else:
            raise Exception
