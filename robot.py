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

        # Prepare the info needed for sensors and motors in the bots
        self.Prepare_To_Sense()
        self.Prepare_To_Act()

    def Prepare_To_Sense(self):

        for bot in self.bots:
            self.bots[bot].Prepare_To_Sense(self.linkInfo[bot])

        # for linkName in pyrosim.linkNamesToIndices:  # This is created after Prepare_To_Simulate
        #     self.sensors[linkName] = SENSOR(linkName)

    def Sense(self):


        for bot in self.bots:
            self.bots[bot].Sense()
        # for sensor in self.sensors:
        #     print("Robot: " + str(self.sensors[sensor]) + ' link: ' + str(sensor) + ' Value: ' + str(self.sensors[sensor].Get_Value()))

    def Prepare_To_Act(self):

        for bot in self.bots:
            self.bots[bot].Prepare_To_Act(self.jointInfo[bot])

    def Think(self):
        self.nn.Update()
        #self.nn.Print()

    def Act(self, time_stamp):
        # for neuronName in self.nn.Get_Neuron_Names():
        #     if self.nn.Is_Motor_Neuron(neuronName):
        #         jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
        #         desiredAngle = self.nn.Get_Value_Of(neuronName) * c.motorJointRange
        #         self.motors[jointName].Set_Value(self.robotID, desiredAngle)

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

    def Prepare_To_Sense(self, linkInfo):
        self.sensors = {}
        for linkName in linkInfo:
            self.sensors[linkName] = SENSOR(linkName)

    def Prepare_To_Act(self, jointInfo):
        self.motors = {}
        for jointName in jointInfo:
            self.motors[jointName] = MOTOR(jointName, self.robotID)

    def Sense(self):
        for sensor in self.sensors:
            print("Robot: " + str(self.robotID) + ' link: ' + str(sensor) + ' Value: ' + str(self.sensors[sensor].Get_Value()))

    def Act(self, time_stamp):

        if c.MOTION_TYPE == 'oscillatory':

            for neuronName in self.nn.Get_Neuron_Names():
                if self.nn.Is_Motor_Neuron(neuronName):
                    jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                    self.motors[jointName].Set_Value(self.robotID, time_stamp)

        elif c.MOTION_TYPE == 'ragdoll':
            pass