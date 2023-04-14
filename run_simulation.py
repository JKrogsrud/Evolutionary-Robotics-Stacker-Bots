import pybullet as p
import pybullet_data

import pyrosim.pyrosim as pyrosim
from simulation import SIMULATION
import constants as c

from world import WORLD
from robot import ROBOTSWARM
from robot import ROBOT
from robot import HIVE_MIND

from sensor import SENSOR
from motor import MOTOR

from pyrosim.neuralNetwork import NEURAL_NETWORK

simlength = 10000

### Looks for files named brain_* with the given solutionID
def run_simulation(numBots, solutionID):
    directOrGUI = 'GUI'
    solutionID = solutionID
    bodyType = 'A'
    numBots = c.numBots

    simulation = SIMULATION(directOrGUI, solutionID, bodyType, numBots)
    simulation.run()

def run_best():
    if c.BRAIN_TYPE == 'hive_mind':
        physicsClient = p.connect(p.GUI)

        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(c.X_GRAV, c.Y_GRAV, c.Z_GRAV)

        world = WORLD()

        hive_mind = HIVE_MIND(1, c.bodytype, c.numBots, best=True)

        # Run it
        for t in range(simlength-1):
            p.stepSimulation()
            hive_mind.Sense(t)
            hive_mind.Think()
            hive_mind.Act(t)

        # Print motor and sensor values to a csv
        f = open('run_data.txt', 'w')

        for bot in hive_mind.bots:
            for sensor in hive_mind.bots[bot]['sensors']:
                f.write(hive_mind.bots[bot]['sensors'][sensor].linkName)
                f.write(str(hive_mind.bots[bot]['sensors'][sensor].values))
                f.write('\n')
            for motor in hive_mind.bots[bot]['motors']:
                f.write(hive_mind.bots[bot]['motors'][motor].jointName)
                f.write(str(hive_mind.bots[bot]['motors'][motor].values))
                f.write('\n')

        # TODO: Here we will print the neural network into f as well

        f.close()

    else:
        physicsClient = p.connect(p.GUI)

        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(c.X_GRAV, c.Y_GRAV, c.Z_GRAV)

        world = WORLD()

        bots = {}

        # Load bots and neural networks
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
        for t in range(simlength):
            p.stepSimulation()
            for bot in bots:
                bots[bot].Sense(t)
                bots[bot].Think()
                bots[bot].Act(t)

        # Save Values to a doc
        f = open('run_data.txt', 'w')

        for bot in bots:
            for sensor in bots[bot].sensors:
                f.write(bots[bot].sensors[sensor].linkName)
                f.write(str(bots[bot].sensors[sensor].values))
            for motor in bots[bot].motors:
                f.write(bots[bot].motors[motor].jointName)
                f.write(str(bots[bot].motors[motor].values))

        # TODO: Print the NN to the run_data.txt file

        f.close()

run_best()
