from simulation import SIMULATION
import constants as c

### Looks for files named brain_* with the given solutionID
def run_simulation(numBots, solutionID):
    directOrGUI = 'GUI'
    solutionID = solutionID
    bodyType = 'A'
    numBots = c.numBots

    simulation = SIMULATION(directOrGUI, solutionID, bodyType, numBots)
    simulation.run()

###
run_simulation(3, 496)