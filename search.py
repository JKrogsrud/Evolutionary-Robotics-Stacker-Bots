import os
from hillclimber import HILLCLIMBER
from parallelHillClimber import PARALLEL_HILLCLIMBER
from surviveAndMultiply import SURVIVE_MULTIPLY
import constants as c
import time

if c.evolutionaryAlgorithm == 'PHC':
    start_time = time.time()
    phc = PARALLEL_HILLCLIMBER(c.bodytype, c.numBots)
    phc.Evolve()

    end_time = time.time()

    # phc.Show_Best()
    phc.Save_Best()
elif c.evolutionaryAlgorithm == 'SAM':
    start_time = time.time()
    phc = PARALLEL_HILLCLIMBER(c.bodytype, c.numBots)
    phc.Evolve()

    end_time = time.time()

    # phc.Show_Best()
    phc.Save_Best()

# save an info document relaying some information about this run

print("Number of generations: " + str(c.numberOfGenerations))
print("Population per generation: " + str(c.populationSize))
print("Time:")
print(end_time - start_time)
