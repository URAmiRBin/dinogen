from game import Game
import numpy as np
import random

POPULATION = 300
GENERATIONS = 10
MUT_PROB = 0.4

g = Game(["00001000100010010002010102"])
g.set_level_index(0)
fitness_list = []

generation = [''.join(np.random.choice(['0', '1', '2'], 26, p=[0.34, 0.33, 0.33])) for _ in range(POPULATION)]

def calculate_fitness(generation):
    result = []
    for chromosome in generation:
        result.append(g.get_score(chromosome)[1])
    return result

def selection(generation, fitness_list):
    return sorted(range(POPULATION), key=lambda k: fitness_list[k], reverse=True)[0:int(POPULATION/2)]
    
def crossover(generation, parents_indices):
    parents = [generation[i] for i in parents_indices]
    newgen = parents
    cut_point = int(len(generation[0])/2)
    shuffled_parents = parents[:]
    random.shuffle(shuffled_parents)
    for i in range(0, len(parents), 2):
        p1 = shuffled_parents[i]
        p2 = shuffled_parents[i + 1]
        o1 = p1[0:cut_point] + p2[cut_point:]
        o2 = p2[0:cut_point] + p1[cut_point:]
        newgen.append(o1)
        newgen.append(o2)
    return newgen

def mutation(generation):
    x = len(generation[0])
    mutants = np.random.randint(int(POPULATION/2), int(POPULATION), size=int(MUT_PROB * POPULATION/2,))
    for mutant in mutants:
        r = [random.randint(0, x)][0]
        generation[mutant] = generation[mutant][0:r] + '0' + generation[mutant][r+1:]

for i in range(GENERATIONS):
    fitness = calculate_fitness(generation)
    survivors_indices = selection(generation, fitness)
    generation = crossover(generation, survivors_indices)
    mutation(generation)