import os
from hillclimber import HILLCLIMBER
from parallelHillClimber import PARALLEL_HILLCLIMBER
import constants as c
import time

start_time = time.time()
phc = PARALLEL_HILLCLIMBER(c.bodytype, c.numBots)

phc.Evolve()

end_time = time.time()

phc.Show_Best()
# phc.Save_Best()

print("Number of generations: " + str(c.numberOfGenerations))
print("Population per generation: " + str(c.populationSize))
print("Time:")
print(end_time - start_time)
