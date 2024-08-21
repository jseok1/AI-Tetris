import random

from tetromino import Tetromino

TETROMINOES = [
    [
        [(-2, 0), (-1, 0), (0, 0), (1, 0)],
        [(0, -2), (0, -1), (0, 0), (0, 1)]
    ],
    [
        [(-1, 0), (0, 0), (1, 0), (1, 1)],
        [(0, -1), (0, 0), (-1, 1), (0, 1)],
        [(-1, -1), (-1, 0), (0, 0), (1, 0)],
        [(0, -1), (1, -1), (0, 0), (0, 1)]
    ],
    [
        [(-1, 0), (0, 0), (1, 0), (-1, 1)],
        [(-1, -1), (0, -1), (0, 0), (0, 1)],
        [(1, -1), (-1, 0), (0, 0), (1, 0)],
        [(0, -1), (0, 0), (0, 1), (1, 1)]
    ],
    [
        [(-1, 0), (0, 0), (-1, 1), (0, 1)]
    ],
    [
        [(0, 0), (1, 0), (-1, 1), (0, 1)],
        [(0, -1), (0, 0), (1, 0), (1, 1)]
    ],
    [
        [(-1, 0), (0, 0), (0, 1), (1, 1)],
        [(1, -1), (0, 0), (1, 0), (0, 1)]
    ],
    [
        [(-1, 0), (0, 0), (1, 0), (0, 1)],
        [(0, -1), (-1, 0), (0, 0), (0, 1)],
        [(-1, 0), (0, 0), (1, 0), (0, -1)],
        [(0, -1), (0, 0), (1, 0), (0, 1)] 
    ]
]


class Randomizer:

    def __init__(self, seed):
        self.previous_tetromino = 0
        random.seed(seed)

    def get_tetromino(self):
        """Return a pseudo-random tetromino."""
        tetromino = random.randint(1, 8)
        if tetromino == self.previous_tetromino or tetromino == 8:
            tetromino = random.randint(1, 7)
        self.previous_tetromino = tetromino
        return Tetromino(tetromino, 5, 2, 0, TETROMINOES[tetromino - 1])
