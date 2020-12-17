import random

import Tetromino

TETROMINOES = {'I': [['....',
                      '....',
                      'IIII',
                      '....'],
                     ['..I.',
                      '..I.',
                      '..I.',
                      '..I.']],
               'J': [['....',
                      '.JJJ',
                      '...J',
                      '....'],
                     ['..J.',
                      '..J.',
                      '.JJ.',
                      '....'],
                     ['.J..',
                      '.JJJ',
                      '....',
                      '....'],
                     ['..JJ',
                      '..J.',
                      '..J.',
                      '....']],
               'L': [['....',
                      '.LLL',
                      '.L..',
                      '....'],
                     ['.LL.',
                      '..L.',
                      '..L.',
                      '....'],
                     ['...L',
                      '.LLL',
                      '....',
                      '....'],
                     ['..L.',
                      '..L.',
                      '..LL',
                      '....']],
               'O': [['....',
                      '.OO.',
                      '.OO.',
                      '....']],
               'S': [['....',
                      '..SS',
                      '.SS.',
                      '....'],
                     ['..S.',
                      '..SS',
                      '...S',
                      '....']],
               'Z': [['....',
                      '.ZZ.',
                      '..ZZ',
                      '....'],
                     ['...Z',
                      '..ZZ',
                      '..Z.',
                      '....']],
               'T': [['....',
                      '.TTT',
                      '..T.',
                      '....'],
                     ['..T.',
                      '.TT.',
                      '..T.',
                      '....'],
                     ['..T.',
                      '.TTT',
                      '....',
                      '....',],
                     ['..T.',
                      '..TT',
                      '..T.',
                      '....']]}


class Randomizer:

    def __init__(self):
        self.bag = []

    def get_tetromino(self, classic=False):
        """Return a pseudo-random tetromino using the 7-bag algorithm."""
        if len(self.bag) == 0:
            self.bag = ['I', 'J', 'L', 'O', 'S', 'Z', 'T']
            random.shuffle(self.bag)
        return Tetromino.Tetromino(3, 0, 0, TETROMINOES[self.bag.pop()], 4)
