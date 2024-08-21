import random

from os import environ

environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"

from joblib import Parallel, delayed

from tetris import Tetris
from agent import Agent

POPULATION = 40
GENERATIONS = 15

CROSSOVER_CHANCE = 0.85
MUTATION_CHANCE = 0.05

WIDTH = 10
HEIGHT = 20


class Chromosome:
  def __init__(self, chromosome):
    self.chromosome = chromosome
    self.fitness = 0


class Trainer:
  def __init__(self):
    self.chromosomes = [
      Chromosome([random.uniform(-1, 1) for _ in range(4)]) for _ in range(POPULATION)
    ]

  def select(self):
    """Simulate the selection genetic operator."""
    self.chromosomes.sort(key=lambda chromosome: chromosome.fitness)
    self.chromosomes = self.chromosomes[::-1][: POPULATION // 2]

  def crossover(self, pool):
    """Simulate the crossover genetic operator."""
    parents = [random.choice(pool), random.choice(pool)]
    children = []
    if random.random() < CROSSOVER_CHANCE:
      i = random.randint(0, 3)
      children.append(Chromosome(parents[0].chromosome[:i] + parents[1].chromosome[i:]))
      children.append(Chromosome(parents[1].chromosome[:i] + parents[0].chromosome[i:]))
    else:
      children.append(Chromosome(parents[0].chromosome[:]))
      children.append(Chromosome(parents[1].chromosome[:]))
    return children

  def mutate(self, chromosome):
    """Simulate the mutation genetic operator."""
    for i in range(4):
      if random.random() < MUTATION_CHANCE:
        chromosome.chromosome[i] = random.uniform(-1, 1)

  def get_fitness(self, chromosome, seed):
    """Return the fitness of a given chromosome."""
    agent = Agent(chromosome.chromosome)
    game = Tetris(WIDTH, HEIGHT, 0, 0, seed)  # simulate a game of Tetris
    while game.state != 0:
      agent.play(game.curr_tetromino, game.grid)(game)
      game.update()
    chromosome.fitness = game.score.score
    print(f"Fitness: {chromosome.fitness}")
    return chromosome

  def simulate(self):
    """Return an optimal set of weights for an agent playing a game of Tetris."""
    for i in range(GENERATIONS):
      print(f"=== Generation {i} ===\n")
      seed = random.randint(0, 99)
      self.chromosomes = Parallel(n_jobs=-1)(
        delayed(self.get_fitness)(chromosome, seed) for chromosome in self.chromosomes
      )
      self.select()
      pool = self.chromosomes[:]
      while len(self.chromosomes) < POPULATION:
        chromosomes = self.crossover(pool)
        for chromosome in chromosomes:
          self.mutate(chromosome)
        self.chromosomes.extend(chromosomes)
      print()
    return max(self.chromosomes, key=lambda chromosome: chromosome.fitness).chromosome


if __name__ == "__main__":
  trainer = Trainer()
  weights = trainer.simulate()
  print(f"Weights: {weights}")
  with open("weights.txt", "w") as f:
    f.write(",".join(weights))
