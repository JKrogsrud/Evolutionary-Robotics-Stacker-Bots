import pybullet as p
import pyrosim.pyrosim as pyrosim
import constants as c
import numpy as np
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os

from sensor import SENSOR
from motor import MOTOR

class HIVE_MIND:
    def __init__(self, solutionID, bodyType, numBots, best=False):
        self.bodyType = bodyType
        self.numBots = int(numBots)
        self.solutionID = int(solutionID)

        self.bots = {}

        for botNum in range(self.numBots):
            robotID = p.loadURDF("body_" + self.bodyType + str(botNum) + ".urdf")
            botDict = {}
            botDict['robotID'] = robotID
            self.bots[robotID] = botDict
        if best:
            self.hiveMind = NEURAL_NETWORK("best_brain.nndf")
        else:
            self.hiveMind = NEURAL_NETWORK("brain_" + str(self.solutionID) + str(self.bodyType) + ".nndf")

        self.linkInfo, self.jointInfo = pyrosim.Prepare_To_Simulate(list(self.bots.keys()))

        self.Prepare_To_Sense()
        self.Prepare_To_Act()

    def Prepare_To_Sense(self):

        for bot in self.bots:
            sensors = {}
            robotID = self.bots[bot]['robotID']
            for linkName in self.linkInfo[bot]:
                sensors[linkName] = SENSOR(linkName, robotID)
            self.bots[bot]['sensors'] = sensors

    def Prepare_To_Act(self):

        for bot in self.bots:
            motors = {}
            robotID = self.bots[bot]['robotID']
            for jointName in self.jointInfo[bot]:
                motors[jointName] = MOTOR(jointName, robotID)
            self.bots[bot]['motors'] = motors

    # Data Reporting
    def Sense(self, t):
        # Record Sensor data at every sense interval
        for bot in self.bots:
            for sensor in self.bots[bot]['sensors']:
                self.bots[bot]['sensors'][sensor].Record_Value(t)

            for motor in self.bots[bot]['motors']:
                self.bots[bot]['motors'][motor].Record_Value(t)

    def Act(self, time_stamp):
        for neuronName in self.hiveMind.Get_Neuron_Names():
            if self.hiveMind.Is_Motor_Neuron(neuronName):

                jointName = self.hiveMind.Get_Motor_Neurons_Joint(neuronName)

                # Need to change the angles that are allowed per joint
                # Lets do this by a dictionary in the constants
                # NOTE: THIS WILL LIMIT NUMBOTS TO 9 BUT DOUBT I CAN GET
                #       THOSE KIND OF RESULTS ANYWAYS

                jointTypes = str(jointName).split('_')
                botNum = int(jointTypes[0][0]) + 1
                jointType = jointTypes[0][1:] + '_' + jointTypes[1][1:]

                lower_bound = c.motorJointRanges[jointType][0]
                upper_bound = c.motorJointRanges[jointType][1]

                desiredAngle = ((self.hiveMind.Get_Value_Of(neuronName) + 1) / 2) * (upper_bound - lower_bound) + lower_bound

                self.bots[botNum]['motors'][jointName].Set_Value_NN(botNum, desiredAngle)

    def Think(self):

        # Updated Update to not need bot info
        self.hiveMind.Update(0)

    def Get_Fitness(self):

        coords = np.empty((c.numBots, 3))

        for bot in self.bots:
            basePositionAndOrientation = p.getBasePositionAndOrientation(self.bots[bot]['robotID'])
            basePosition = basePositionAndOrientation[0]  # Cartesian coordinates
            coords[bot-1, :] = np.array(basePosition)

        # Find the middle
        sums = np.sum(a=coords, axis=0)
        midpoint = sums / c.numBots

        # Numpy is amazing
        delta = coords - midpoint
        dist = np.sqrt(np.sum(delta*delta, 1))

        fitness = 1
        for i in range(c.numBots):
            fitness *= (1.0 / (dist[i]+1))

        f = open("tmp" + str(self.solutionID) + ".txt", "w")
        f.write(str(fitness))
        f.close()

        os.rename("tmp" + str(self.solutionID) + ".txt", "fitness" + str(self.solutionID) + ".txt")

class ROBOTSWARM:

    def __init__(self, solutionID, bodyType, numBots):
        self.bodyType = bodyType
        self.numBots = int(numBots)
        self.solutionID = int(solutionID)

        self.bots = {}

        # if c.BRAIN_TYPE == 'neural_network':
        for botNum in range(self.numBots):
            robotID = p.loadURDF("body_" + self.bodyType + str(botNum) + ".urdf")
            robotNN = NEURAL_NETWORK("brain_" + str(self.solutionID) + str(self.bodyType) + str(botNum) + ".nndf")
            self.bots[robotID] = ROBOT(robotID, robotNN)


        self.linkInfo, self.jointInfo = pyrosim.Prepare_To_Simulate(list(self.bots.keys()))

        #TODO: Double check the necessity of this?
        #       It appears to be send ALL joint info to each bot
        for bot in self.bots:
            self.bots[bot].Set_Number_links(self.jointInfo["numJoints"])

        # Prepare the info needed for sensors and motors in the bots
        self.Prepare_To_Sense()
        self.Prepare_To_Act()

    def Prepare_To_Sense(self):

        for bot in self.bots:
            self.bots[bot].Prepare_To_Sense(self.linkInfo[bot])

    def Sense(self, t):

        for bot in self.bots:
            self.bots[bot].Sense(t)

    def Prepare_To_Act(self):

        for bot in self.bots:
            self.bots[bot].Prepare_To_Act(self.jointInfo[bot])

    def Think(self):
        for bot in self.bots:
            self.bots[bot].Think()

    def Act(self, time_stamp):

        if c.BRAIN_TYPE == 'ragdoll':
            pass
        elif c.BRAIN_TYPE == 'oscillatory':
            for bot in self.bots:
                self.bots[bot].Act(time_stamp)
        elif c.BRAIN_TYPE == 'rigid':
            for bot in self.bots:
                self.bots[bot].Act(time_stamp)
        elif c.BRAIN_TYPE == 'neural_network':
            for bot in self.bots:
                self.bots[bot].Act(time_stamp)

    def Save_Values(self):

        for sensor in self.sensors:
            self.sensors[sensor].Save_Values()
        for motor in self.motors:
            self.motors[motor].Save_Values()

    def Get_Fitness(self):

        if c.fitness == 'gather':

            bot_info = []
            fitness = 1

            for bot in self.bots:
                bot_info.append(self.bots[bot].Get_Fitness())

            # Higher fitness is awarded to bots that are stacking, so their center of mass should
            # be close to each other

            total_x = 0
            total_y = 0
            for bot in bot_info:
                total_x += bot['position'][0]
                total_y += bot['position'][1]

            mid_x = total_x / self.numBots
            mid_y = total_y / self.numBots

            # find the distance each bot is from that center of mass

            for bot in bot_info:
                distance_from_mid = np.sqrt((mid_x - bot['position'][0])**2 + (mid_y - bot['position'][1])**2)
                # print(distance_from_mid)
                fitness *= 1 / (distance_from_mid + .01)


        if c.fitness == 'top_sensor':

            # Gather sensor data from each bot

            fitness = 0

            for bot in self.bots:
                bot_sensor_data = []
                for sensor in self.bots[bot].sensors:
                    if self.bots[bot].sensors[sensor].linkName[1:] == 'TopSensor':
                        bot_sensor_data = self.bots[bot].sensors[sensor].values
                bot_sensor_data = bot_sensor_data[-int(c.SIM_LEN / c.targetFrames):]

                # Check if it spent most of the last c.SIM_LEN / c.targetFrames frames with it's TopSensor active

                rolling_sum = 0
                for val in bot_sensor_data:
                    if val > 0:
                        rolling_sum += val

                fitness += rolling_sum


        # changed tmp to fitness
        f = open("tmp" + str(self.solutionID) + ".txt", "w")
        f.write(str(fitness))
        f.close()

        os.rename("tmp" + str(self.solutionID) + ".txt", "fitness" + str(self.solutionID) + ".txt")


class ROBOT:

    def __init__(self, robotID, robotNN):
        self.robotID = robotID
        self.nn = robotNN

    def Set_Number_links(self, numLinks):
        self.numLinks = numLinks

    def Prepare_To_Sense(self, linkInfo):
        self.sensors = {}
        for linkName in linkInfo:
            self.sensors[linkName] = SENSOR(linkName, self.robotID)

    def Prepare_To_Act(self, jointInfo):
        self.motors = {}
        for jointName in jointInfo:
            self.motors[jointName] = MOTOR(jointName, self.robotID)

    def Sense(self, t):

        for sensor in self.sensors:
            self.sensors[sensor].Record_Value(t)

        for motor in self.motors:
            self.motors[motor].Record_Value(t)

    def Act(self, time_stamp):

        if c.BRAIN_TYPE == 'oscillatory':

            for neuronName in self.nn.Get_Neuron_Names():
                if self.nn.Is_Motor_Neuron(neuronName):
                    jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                    self.motors[jointName].Set_Value(self.robotID, time_stamp)

        elif c.BRAIN_TYPE == 'ragdoll':
            pass

        elif c.BRAIN_TYPE == 'rigid':

            for neuronName in self.nn.Get_Neuron_Names():
                if self.nn.Is_Motor_Neuron(neuronName):
                    jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                    self.motors[jointName].Set_Value(self.robotID, time_stamp)

        elif c.BRAIN_TYPE == 'neural_network':
            for neuronName in self.nn.Get_Neuron_Names():
                if self.nn.Is_Motor_Neuron(neuronName):

                    jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)

                    # Need to change the angles that are allowed per joint
                    # Lets do this by a dictionary in the constants
                    # NOTE: THIS WILL LIMIT NUMBOTS TO 9 BUT DOUBT I CAN GET
                    #       THOSE KIND OF RESULTS ANYWAYS

                    jointTypes = str(jointName).split('_')
                    jointType = jointTypes[0][1:] + '_' + jointTypes[1][1:]

                    lower_bound = c.motorJointRanges[jointType][0]
                    upper_bound = c.motorJointRanges[jointType][1]

                    desiredAngle = ((self.nn.Get_Value_Of(neuronName) + 1) / 2) * (upper_bound - lower_bound) + lower_bound
                    self.motors[jointName].Set_Value_NN(self.robotID, desiredAngle)

    def Think(self):
        self.nn.Update(self.robotID)

    def Get_Fitness(self):
        # This will likely change over time but I want the evolutionary algorithm
        # working before working on finding the right fitness

        bot_info = {}

        # Get x and y position of bot
        basePositionAndOrientation = p.getBasePositionAndOrientation(self.robotID)
        basePosition = basePositionAndOrientation[0]
        xPosition = basePosition[0]
        yPosition = basePosition[1]

        bot_info['position'] = (xPosition, yPosition)

        # Get which torso sensors are active at the end
        # Don't exactly know how to do this part

        return bot_info
