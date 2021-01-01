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


# class Randomizer:

#     def __init__(self):
#         self.bag = []

#     def get_tetromino(self):
#         """Return a pseudo-random tetromino using the 7-bag algorithm."""
#         if len(self.bag) == 0:
#             self.bag = ['I', 'J', 'L', 'O', 'S', 'Z', 'T']
#             random.shuffle(self.bag)
#         tetromino = self.bag.pop()
#         return Tetromino.Tetromino(3, 0 if tetromino == 'I' else 1, 0, TETROMINOES[tetromino])

class Randomizer:

    def __init__(self):
        self.previous_tetromino = None

    def get_tetromino(self):
        """Return a pseudo-random tetromino."""
        tetromino = random.choice(['I', 'J', 'L', 'O', 'S', 'Z', 'T', ''])
        if tetromino == self.previous_tetromino or not tetromino:
            tetromino = random.choice(['I', 'J', 'L', 'O', 'S', 'Z', 'T'])
        self.previous_tetromino = tetromino
        return Tetromino.Tetromino(3, 0 if tetromino == 'I' else 1, 0, TETROMINOES[tetromino])
