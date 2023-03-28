import pybullet as p
import pyrosim.pyrosim as pyrosim
import constants as c
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os

from sensor import SENSOR
from motor import MOTOR

class ROBOTSWARM:

    def __init__(self, solutionID, bodyType, numBots):
        self.bodyType = bodyType
        self.numBots = numBots
        self.solutionID = solutionID

        self.bots = {}

        for botNum in range(self.numBots):
            robotID = p.loadURDF("body_" + self.bodyType + str(botNum) + ".urdf")
            robotNN = NEURAL_NETWORK("brain_" + str(self.solutionID) + str(self.bodyType) + str(botNum) + ".nndf")
            self.bots[robotID] = ROBOT(robotID, robotNN)

        #os.system("del brain" + str(self.solutionID) + ".nndf")

        self.linkInfo, self.jointInfo = pyrosim.Prepare_To_Simulate(list(self.bots.keys()))
        # print(self.linkInfo)
        # print(self.jointInfo)

        for bot in self.bots:
            self.bots[bot].Set_Number_links(self.jointInfo["numJoints"])

        # Prepare the info needed for sensors and motors in the bots
        self.Prepare_To_Sense()
        self.Prepare_To_Act()

    def Prepare_To_Sense(self):

        for bot in self.bots:
            # print("Prepare_To_Sense")
            # print(bot)
            self.bots[bot].Prepare_To_Sense(self.linkInfo[bot])
            # print(self.linkInfo[bot])

        # for linkName in pyrosim.linkNamesToIndices:  # This is created after Prepare_To_Simulate
        #     self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, t):

        for bot in self.bots:
            self.bots[bot].Sense(t)

        # for sensor in self.sensors:
        #     print("Robot: " + str(self.sensors[sensor]) + ' link: ' + str(sensor) + ' Value: ' + str(self.sensors[sensor].Get_Value()))

    def Prepare_To_Act(self):

        for bot in self.bots:
            self.bots[bot].Prepare_To_Act(self.jointInfo[bot])

    def Think(self):
        for bot in self.bots:
            self.bots[bot].Think()

    def Act(self, time_stamp):

        if c.MOTION_TYPE == 'ragdoll':
            pass
        elif c.MOTION_TYPE == 'oscillatory':
            for bot in self.bots:
                self.bots[bot].Act(time_stamp)
        elif c.MOTION_TYPE == 'rigid':
            for bot in self.bots:
                self.bots[bot].Act(time_stamp)
        elif c.MOTION_TYPE == 'neural_network':
            for bot in self.bots:
                self.bots[bot].Act(time_stamp)

    def Save_Values(self):

        for sensor in self.sensors:
            self.sensors[sensor].Save_Values()
        for motor in self.motors:
            self.motors[motor].Save_Values()

    def Get_Fitness(self):

        basePositionAndOrientation = p.getBasePositionAndOrientation(self.robotID)
        basePosition = basePositionAndOrientation[0]
        xPosition = basePosition[0]

        f = open("tmp" + str(self.solutionID) + ".txt", "w")
        f.write(str(xPosition))
        f.close()

        os.rename("tmp"+ str(self.solutionID) + ".txt", "fitness" + str(self.solutionID) + ".txt")

class ROBOT:

    def __init__(self, robotID, robotNN):
        self.robotID = robotID
        self.nn = robotNN

    def Set_Number_links(self, numLinks):
        self.numLinks = numLinks

    def Prepare_To_Sense(self, linkInfo):
        self.sensors = {}
        for linkName in linkInfo:
            # print(linkName)
            self.sensors[linkName] = SENSOR(linkName, self.robotID, self.numLinks)
        # print("Bot " + str(self.robotID) + " Sensor set up: " + str(linkName))

    def Prepare_To_Act(self, jointInfo):
        self.motors = {}
        for jointName in jointInfo:
            self.motors[jointName] = MOTOR(jointName, self.robotID)

    def Sense(self, t):
        if t % c.senseTiming == 0:
            print("-")
        for sensor in self.sensors:
            if t % c.senseTiming == 0:
                if self.sensors[sensor].Get_Value() != -1.0:
                    print("Robot: " + str(self.robotID) + ' link: ' + str(sensor) + ' Value: ' + str(self.sensors[sensor].Get_Value()))

    def Act(self, time_stamp):

        if c.MOTION_TYPE == 'oscillatory':

            for neuronName in self.nn.Get_Neuron_Names():
                if self.nn.Is_Motor_Neuron(neuronName):
                    jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                    self.motors[jointName].Set_Value(self.robotID, time_stamp)

        elif c.MOTION_TYPE == 'ragdoll':
            pass

        elif c.MOTION_TYPE == 'rigid':

            for neuronName in self.nn.Get_Neuron_Names():
                if self.nn.Is_Motor_Neuron(neuronName):
                    jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                    self.motors[jointName].Set_Value(self.robotID, time_stamp)

        elif c.MOTION_TYPE == 'neural_network':
            for neuronName in self.nn.Get_Neuron_Names():
                if self.nn.Is_Motor_Neuron(neuronName):
                    # print("Neuron name: " + str(neuronName))
                    jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                    desiredAngle = self.nn.Get_Value_Of(neuronName) * c.motorJointRange
                    # print("Motor name: " + str(self.motors[jointName].jointName))
                    # print("Desired Angle: " + str(desiredAngle))
                    self.motors[jointName].Set_Value_NN(self.robotID, desiredAngle)

    def Think(self):
        self.nn.Update(self.robotID)