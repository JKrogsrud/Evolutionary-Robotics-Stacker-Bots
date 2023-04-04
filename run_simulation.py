import pybullet as p
import pybullet_data

import pyrosim.pyrosim as pyrosim
from simulation import SIMULATION
import constants as c

from world import WORLD
from robot import ROBOTSWARM
from robot import ROBOT

from sensor import SENSOR
from motor import MOTOR

from pyrosim.neuralNetwork import NEURAL_NETWORK

### Looks for files named brain_* with the given solutionID
def run_simulation(numBots, solutionID):
    directOrGUI = 'GUI'
    solutionID = solutionID
    bodyType = 'A'
    numBots = c.numBots

    simulation = SIMULATION(directOrGUI, solutionID, bodyType, numBots)
    simulation.run()

def run_best():
    physicsClient = p.connect(p.GUI)

    p.setAdditionalSearchPath(pybullet_data.getDataPath())
    p.setGravity(c.X_GRAV, c.Y_GRAV, c.Z_GRAV)

    world = WORLD()

    bots = {}

    for botNum in range(c.numBots):
        robotID = p.loadURDF("body_A" + str(botNum) + ".urdf")
        robotNN = NEURAL_NETWORK("best_brain_" + str(botNum) + ".nndf")
        bots[robotID] = ROBOT(robotID, robotNN)

    linkInfo, jointInfo = pyrosim.Prepare_To_Simulate(bots.keys())

    for bot in bots:
        bots[bot].Set_Number_links(jointInfo["numJoints"])

    for bot in bots:
        bots[bot].Prepare_To_Sense(linkInfo[bot])

    for bot in bots:
        bots[bot].Prepare_To_Act(jointInfo[bot])

    # Run it
    for t in range(c.SIM_LEN):
        p.stepSimulation()
        for bot in bots:
            bots[bot].Sense(t)
            bots[bot].Think()
            bots[bot].Act(t)


run_best()
