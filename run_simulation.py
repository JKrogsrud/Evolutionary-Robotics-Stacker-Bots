import pybullet as p
import pybullet_data

import datetime
import os
import numpy as np

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

simlength = c.SIM_LEN

### Looks for files named brain_* with the given solutionID
def run_simulation(numBots, solutionID):
    directOrGUI = 'GUI'
    solutionID = solutionID
    bodyType = 'A'
    numBots = c.numBots

    simulation = SIMULATION(directOrGUI, solutionID, bodyType, numBots)
    simulation.run()

def run_best():

    # First we prep the directory for data storage in an organized fashion
    today = datetime.datetime.now()
    month = today.month
    day = today.day
    hour = today.time().hour
    minute = today.time().minute

    # Creating Directory
    dir_name = 'data/' + str(month) + '_' + str(day) + '_' + str(hour) + '_' + str(minute)
    current_dir = os.getcwd()
    path = os.path.join(current_dir, dir_name)

    os.mkdir(path)
    if c.BRAIN_TYPE in {'hive_mind', 'hive_mind_recurrant', 'hive_mind_recurrant_hybrid_A',
                        'hive_mind_recurrant_hybrid_B'}:
        physicsClient = p.connect(p.GUI)

        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(c.X_GRAV, c.Y_GRAV, c.Z_GRAV)

        world = WORLD()

        hive_mind = HIVE_MIND(1, c.bodytype, c.numBots, best=True)

        # Position Data:
        """
        bot:
           | 0 | 1 | 2 |  ....  | c.SIM_LEN
         x |
         y |
         z |
         p |
         t |
         ya|
         
        array_size should be (c.numBots, 6, c.SIM_LEN)
        """

        position_data = np.zeros((c.numBots, 6, c.SIM_LEN))

        # Run it
        #TODO: Change simlength to c.SIM_LEN once we get started
        for t in range(simlength-1):
            p.stepSimulation()
            hive_mind.Sense(t)
            hive_mind.Think(t)
            hive_mind.Act(t)
            positionAndOrientation = hive_mind.Report()
            for botNum in range(c.numBots):
                position_data[botNum, :, t] = positionAndOrientation[0, :]

        np.save(dir_name + '/positions', position_data)

        for bot in hive_mind.bots:
            for sensor in hive_mind.bots[bot]['sensors']:
                sensor_name = hive_mind.bots[bot]['sensors'][sensor].linkName
                sensor_values = hive_mind.bots[bot]['sensors'][sensor].values
                np.save(dir_name + '/' + sensor_name + '.npy', sensor_values)
            for motor in hive_mind.bots[bot]['motors']:
                motor_name = hive_mind.bots[bot]['motors'][motor].jointName
                motor_values = hive_mind.bots[bot]['motors'][motor].values
                np.save(dir_name + '/' + motor_name + '.npy', motor_values)

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
            bots[bot].Set_Number_links(jointInfo['numJoints'])

        for bot in bots:
            bots[bot].Prepare_To_Sense(linkInfo[bot])

        for bot in bots:
            bots[bot].Prepare_To_Act(jointInfo[bot])

        position_data = np.zeros((c.numBots, 6, c.SIM_LEN))

        # Run it
        for t in range(simlength):
            p.stepSimulation()
            for bot in bots:
                bots[bot].Sense(t)
                bots[bot].Think(t)
                bots[bot].Act(t)

                bot_info = p.getBasePositionAndOrientation(bots[bot].robotID)
                bot_pos = list(bot_info[0])
                bot_orientations = list(p.getEulerFromQuaternion(bot_info[1]))
                bot_pos.extend(bot_orientations)
                position_data[bot-1, :, t] = np.array(bot_pos)

        np.save(dir_name + '/positions.npy', position_data)

        # Save data
        for bot in bots:
            for sensor in bots[bot].sensors:
                sensor_name = bots[bot].sensors[sensor].linkName
                sensor_values = bots[bot].sensors[sensor].values
                np.save(dir_name + '/' + sensor_name + '.npy', sensor_values)

            for motor in bots[bot].motors:
                motor_name = bots[bot].motors[motor].jointName
                motor_values = bots[bot].motors[motor].values
                np.save(dir_name + '/' + motor_name + '.npy', motor_values)


run_best()
