import os
from hillclimber import HILLCLIMBER
from parallelHillClimber import PARALLEL_HILLCLIMBER
from surviveAndMultiply import SURVIVE_MULTIPLY
from noEvolution import RANDOM_NETWORKS
import constants as c
import time

def Save_Parameters(time):
    f = open('data.txt', 'w')
    f.write('SIM_LEN:' + str(c.SIM_LEN) + '\n' +
            'BRAIN_TYPE:' + str(c.BRAIN_TYPE) + '\n' +
            'SIM_LEN:' + str(c.SIM_LEN) + '\n' +
            'numSensorNeurons:' + str(c.numSensorNeurons) + '\n' +
            'numHiddenNeurons:' + str(c.numHiddenNeurons) + '\n' +
            'numMotorNeurons:' + str(c.numMotorNeurons) + '\n' +
            'numberOfGenerations:' + str(c.numberOfGenerations) + '\n' +
            'populationSize:' + str(c.populationSize) + '\n' +
            'evolutionaryAlogrithm:' + str(c.evolutionaryAlgorithm) + '\n'
            'numbots:' + str(c.numBots) + '\n' +
            'timeTaken:' + str(time) + '\n')
    f.close()


if c.evolutionaryAlgorithm == 'PHC':
    start_time = time.time()
    phc = PARALLEL_HILLCLIMBER(c.bodytype, c.numBots)
    phc.Evolve()

    end_time = time.time()

    phc.Save_Best()
    Save_Parameters(end_time - start_time)

elif c.evolutionaryAlgorithm == 'SAM':

    start_time = time.time()
    sam = SURVIVE_MULTIPLY(c.bodytype, c.numBots)
    sam.Evolve()

    end_time = time.time()

    sam.Save_Best()
    Save_Parameters(end_time - start_time)

elif c.evolutionaryAlgorithm == 'NONE':
    no_evol = RANDOM_NETWORKS(c.bodytype, c.numBots)
    no_evol.Evolve()
    no_evol.Save()


# save an info document relaying some information about this run
if c.evolutionaryAlgorithm == 'PHC' or c.evolutionaryAlgorithm == 'SAM':
    print("Number of generations: " + str(c.numberOfGenerations))
    print("Population per generation: " + str(c.populationSize))
    print("Time:")
    print(end_time - start_time)
else:
    print('DONE')
