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
            # Set up bots to not be dormant. This will be set to true
            botDict['dormant'] = False
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

                jointTypes = str(jointName).split('_')
                botNum = int(jointTypes[0][0]) + 1

                jointType = jointTypes[0][1:] + '_' + jointTypes[1][1:]

                # Check if bot is dormant
                if self.bots[botNum]['dormant']:
                    # Use lookup for various joints for the correct position
                    desiredAngle = c.dormantMotorJointValues[jointType]
                else:
                    lower_bound = c.motorJointRanges[jointType][0]
                    upper_bound = c.motorJointRanges[jointType][1]

                    desiredAngle = ((self.hiveMind.Get_Value_Of(neuronName) + 1) / 2) * (upper_bound - lower_bound) + lower_bound

                self.bots[botNum]['motors'][jointName].Set_Value_NN(botNum, desiredAngle)

    def Think(self, time_stamp):
        # Updated Update to not need bot info
        self.hiveMind.Update(0)

        # Update dormancy here
        for bot in self.bots:
            robotID = self.bots[bot]['robotID']
            location_of_bot = p.getBasePositionAndOrientation(robotID)[0]
            distance = np.sqrt((location_of_bot[0] - c.goal[0])**2 + (location_of_bot[1]- c.goal[1])**2)
            if distance < c.goalDistance and not self.bots[bot]['dormant']:
                self.bots[bot]['dormant'] = True
                self.bots[bot]['dormantTime'] = time_stamp

    # returns an array of each bots cartesian coordinates and orientation
    def Report(self):
        bot_data = np.zeros((c.numBots, 6))

        for bot in self.bots:
            basePositionAndOrientation = p.getBasePositionAndOrientation(self.bots[bot]['robotID'])
            basePosition = list(basePositionAndOrientation[0])
            baseOrientation = list(p.getEulerFromQuaternion(basePositionAndOrientation[1]))
            basePosition.extend(baseOrientation)
            bot_data[bot-1, :] = np.array(basePosition)

        return bot_data

    def Get_Fitness(self):
        if c.fitness == 'top_sensor_1':

            # Calculate sensor fitness
            sensor_fitness = 0

            for bot in self.bots:
                bot_sensor_data = []
                for sensor in self.bots[bot]['sensors']:
                    if self.bots[bot]['sensors'][sensor].linkName[1:] == 'TopSensor':
                        bot_sensor_data = self.bots[bot]['sensors'][sensor].values
                bot_sensor_data = bot_sensor_data[-int(c.SIM_LEN / c.targetFrames):]

                # Check if it spent most of the last c.SIM_LEN / c.targetFrames with
                # topSensor Active

                rolling_sum = 0
                for val in bot_sensor_data:
                    if val > 0:
                        rolling_sum += val

                sensor_fitness += (rolling_sum / (c.SIM_LEN / c.targetFrames))

            # Calculate the Gather fitness with flip penalty
            bot_positions = []
            bot_orientations = []

            for bot in self.bots:
                bot_positions.append(p.getBasePositionAndOrientation(self.bots[bot]['robotID'])[0])
                bot_orientations.append(p.getEulerFromQuaternion(p.getBasePositionAndOrientation(self.bots[bot]['robotID'])[1]))

            total_flip_penalty = 0
            # orientation is in terms of roll about x
            # pitch about y
            # yaw about z

            for orientation in bot_orientations:
                if orientation[0] > np.pi / 2 or orientation[0] < -np.pi / 2:
                    total_flip_penalty -= c.flipPenalty

            # Calculate distance from (0, 0)
            dist_fitness = 1
            for position in bot_positions:
                dist_fitness *= 1 / (np.sqrt((position[0] - c.goal[0]) ** 2 + (position[1] - c.goal[1]) ** 2) + 1)

            fitness = c.gatherFitnessMultiplier * dist_fitness + total_flip_penalty + c.sensorFitnessMultiplier * sensor_fitness

        if c.fitness == 'gather_and_stack':
            # Repository for all bot fitness's
            allFitness = []
            for bot in self.bots:
                for sensor in self.bots[bot]['sensors']:
                    if self.bots[bot]['sensors'][sensor].linkName[1:] == 'TopSensor':
                        topSensorData = self.bots[bot]['sensors'][sensor].values

                # Total frames where top sensor is active
                topSum = 0
                for val in topSensorData:
                    if val > 0:
                        topSum += val

                sensorFitness = topSum / c.SIM_LEN

                # Calculate distance fitness
                robotID = self.bots[bot]['robotID']
                locationOfBot = p.getBasePositionAndOrientation(robotID)[0]
                distanceToGoal = np.sqrt((locationOfBot[0] - c.goal[0]) ** 2 + (locationOfBot[1] - c.goal[1]) ** 2)

                distanceFitness = 1 / (distanceToGoal + 1)

                # Calculate dormancy fitness
                if self.bots[bot]['dormant']:
                    dormancyFitness = (c.SIM_LEN - self.bots[bot]['dormantTime']) / c.SIM_LEN
                else:
                    dormancyFitness = 0

                # Calculate Flip Penalty
                botOrientation = p.getEulerFromQuaternion(p.getBasePositionAndOrientation(self.bots[bot]['robotID'])[1])
                if botOrientation[0] > np.pi / 2 or botOrientation[0] < -np.pi / 2 or botOrientation[1] > np.pi /2 or botOrientation[1] < -np.pi / 2:
                    flipPenalty = 0
                else:
                    flipPenalty = 1

                # robotFitness = flipPenalty * (c.distanceFitnessWeight * distanceFitness +
                #                               c.sensorFitnessWeight * sensorFitness
                #                               + c.dormancyFitnessWeight * dormancyFitness)

                botFitness = [sensorFitness, distanceFitness, dormancyFitness, flipPenalty]
                allFitness.append(botFitness)

            fitness = 1
            subFitness = []
            # Display the individual bot fitness's
            print("Bot Fitness's for solution: " + str(self.solutionID))
            for i in range(len(allFitness)):
                print(" Bot " + str(i+1) + ":")
                print("\tSensor Fitness:" + str(allFitness[i][0]))
                sensor_fitness = allFitness[i][0]
                print("\tDistance Fitness:" + str(allFitness[i][1]))
                distance_fitness = allFitness[i][1]
                print("\tDormancy Fitness:" + str(allFitness[i][2]))
                dormancy_fitness = allFitness[i][2]
                print("\tFlip Penalty:" + str(allFitness[i][3]))
                flip_penalty = allFitness[i][3]

                robotFitness = allFitness[i][3] * (c.sensorFitnessWeight * allFitness[i][0] +
                                                   c.distanceFitnessWeight * allFitness[i][1] +
                                                   c.dormancyFitnessWeight * allFitness[i][2])
                subFitness.append((robotFitness, (sensor_fitness, distance_fitness, dormancy_fitness, flip_penalty)))
                print("\t\tTotal Fitness = " + str(robotFitness))
                fitness *= robotFitness
            print("\t\t\tTotal Fitness for Solution: " + str(fitness))

        f = open("tmp" + str(self.solutionID) + ".txt", "w")

        f.write(str(fitness) + '\n')
        for botFit in subFitness:
            f.write(str(botFit[0]) + '\n')
            for value in botFit[1]:
                f.write(str(value) + '\n')

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

        # Necessary?
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

    def Think(self, time_stamp):
        for bot in self.bots:
            self.bots[bot].Think(time_stamp)

    def Act(self, time_stamp):
        if c.BRAIN_TYPE == 'neural_network' or c.BRAIN_TYPE == 'neural_network_recurrant':
            for bot in self.bots:
                self.bots[bot].Act(time_stamp)

    def Save_Values(self):

        for sensor in self.sensors:
            self.sensors[sensor].Save_Values()
        for motor in self.motors:
            self.motors[motor].Save_Values()

    def Get_Fitness(self):
        if c.fitness == 'top_sensor_1':

            # Gather sensor data from each bot
            sensor_fitness = 0

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

                sensor_fitness += (rolling_sum / (c.SIM_LEN / c.targetFrames))

            bot_positions = []
            bot_orientations = []

            for bot in self.bots:
                bot_positions.append(p.getBasePositionAndOrientation(self.bots[bot].robotID)[0])
                bot_orientations.append(p.getEulerFromQuaternion(p.getBasePositionAndOrientation(self.bots[bot].robotID)[1]))

            total_flip_penalty = 0
            # orientation is in terms of roll about X, pitch about Y, yaw about Z
            for orientation in bot_orientations:
                # These values range from -pi to pi
                # so we punish for values greater than pi / 2 or less than -pi / 2
                if orientation[0] > np.pi / 2 or orientation[0] < -np.pi / 2:
                    total_flip_penalty -= c.flipPenalty

            # Calculate distance from (0, 0)
            dist_fitness = 1
            for position in bot_positions:
                dist_fitness *= 1 / (np.sqrt((position[0] - c.goal[0])**2 + (position[1] - c.goal[1])**2) + 1)

            fitness = c.gatherFitnessMultiplier * dist_fitness + total_flip_penalty + c.sensorFitnessMultiplier * sensor_fitness

        if c.fitness == "gather_and_stack":
            print("Bot Fitness's for solution: " + str(self.solutionID) + "\n")

            # Gather fitness of all bots
            fitness = 1
            subFitness = []
            for bot in self.bots:
                botID = self.bots[bot].robotID
                botFitness = self.bots[bot].Get_Fitness()
                print(" Bot " + str(botID) + ":")
                print("\tSensor Fitness:" + str(botFitness[0]))
                print("\tDistance Fitness:" + str(botFitness[1]))
                print("\tDormancy Fitness:" + str(botFitness[2]))
                print("\tFlip Penalty:" + str(botFitness[3]))

                robotFitness = botFitness[3] * (c.sensorFitnessWeight * botFitness[0] +
                                                c.distanceFitnessWeight * botFitness[1] +
                                                c.dormancyFitnessWeight * botFitness[2])

                print("\t\tTotal Fitness = " + str(robotFitness))
                subFitness.append((robotFitness, botFitness))
                fitness *= robotFitness
            print("\t\t\tTotal Fitness for Solution: " + str(fitness))

        # changed tmp to fitness
        f = open("tmp" + str(self.solutionID) + ".txt", "w")
        f.write(str(fitness) + '\n')
        for botFit in subFitness:
            f.write(str(botFit[0]) + '\n')
            for value in botFit[1]:
                f.write(str(value) + '\n')
        f.close()

        os.rename("tmp" + str(self.solutionID) + ".txt", "fitness" + str(self.solutionID) + ".txt")


class ROBOT:

    def __init__(self, robotID, robotNN):
        self.robotID = robotID
        self.nn = robotNN
        self.dormant = False

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

        if c.BRAIN_TYPE == 'neural_network' or c.BRAIN_TYPE == 'neural_network_recurrant':
            for neuronName in self.nn.Get_Neuron_Names():
                if self.nn.Is_Motor_Neuron(neuronName):

                    jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)

                    jointTypes = str(jointName).split('_')
                    jointType = jointTypes[0][1:] + '_' + jointTypes[1][1:]

                    if self.dormant:
                        desiredAngle = c.dormantMotorJointValues[jointType]
                    else:
                        lower_bound = c.motorJointRanges[jointType][0]
                        upper_bound = c.motorJointRanges[jointType][1]
                        desiredAngle = ((self.nn.Get_Value_Of(neuronName) + 1) / 2) * (upper_bound - lower_bound) + lower_bound

                    self.motors[jointName].Set_Value_NN(self.robotID, desiredAngle)

    def Think(self, time_stamp):
        self.nn.Update(self.robotID)

        # Determine if bot should be dormant
        bot_position = p.getBasePositionAndOrientation(self.robotID)[0]
        distance = np.sqrt((bot_position[0] - c.goal[0])**2 + (bot_position[1] - c.goal[1])**2)
        if distance < c.goalDistance and not self.dormant:
            self.dormant = True
            self.dormantTime = time_stamp



    def Get_Fitness(self):
        # # This will likely change over time but I want the evolutionary algorithm
        # # working before working on finding the right fitness
        #
        # bot_info = {}
        #
        # # Get x and y position of bot
        # basePositionAndOrientation = p.getBasePositionAndOrientation(self.robotID)
        # basePosition = basePositionAndOrientation[0]
        # xPosition = basePosition[0]
        # yPosition = basePosition[1]
        #
        # bot_info['position'] = (xPosition, yPosition)
        #
        # # Get which torso sensors are active at the end
        # # Don't exactly know how to do this part

        # Get Top Sensor Fitness
        for sensor in self.sensors:
            print()
            if self.sensors[sensor].linkName[1:] == 'TopSensor':
                topSensorData = self.sensors[sensor].values

        topSum = 0
        for val in topSensorData:
            if val > 0:
                topSum += val

        sensorFitness = topSum / c.SIM_LEN

        # Distance fitness:
        locationOfBot = p.getBasePositionAndOrientation(self.robotID)[0]
        distanceToGoal = np.sqrt((locationOfBot[0] - c.goal[0])**2 + (locationOfBot[1] - c.goal[1]) ** 2)

        distanceFitness = 1/ (distanceToGoal + 1)

        # Dormancy Fitness:
        if self.dormant:
            dormancyFitness = (c.SIM_LEN - self.dormantTime) / c.SIM_LEN
        else:
            dormancyFitness = 0

        # Calculate Flip Penalty
        botOrientation = p.getEulerFromQuaternion(p.getBasePositionAndOrientation(self.robotID)[1])
        if botOrientation[0] > np.pi / 2 or botOrientation[0] < - np.pi / 2 or botOrientation[1] > np.pi /2 or botOrientation[1] < -np.pi / 2:
            flipPenalty = 0
        else:
            flipPenalty = 1

        botFitness = [sensorFitness, distanceFitness, dormancyFitness, flipPenalty]

        return botFitness
