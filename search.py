import os
from hillclimber import HILLCLIMBER
from parallelHillClimber import PARALLEL_HILLCLIMBER
import constants as c

phc = PARALLEL_HILLCLIMBER(c.bodytype, c.numBots)

phc.Evolve()

phc.Show_Best()
