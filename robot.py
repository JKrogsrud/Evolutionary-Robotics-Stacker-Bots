import pybullet as p
import pyrosim.pyrosim as pyrosim
import constants as c
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os

from sensor import SENSOR
from motor import MOTOR

class ROBOT:

    def __init__(self, solutionID, bodyType, botNum):
        self.bodyType = bodyType
        self.botNum = botNum
        self.solutionID = solutionID
        # print("body_" + bodyType + str(self.botNum) + ".urdf")
        self.robotID = p.loadURDF("body_" + bodyType + str(self.botNum) + ".urdf")
        self.nn = NEURAL_NETWORK("brain_" + str(self.solutionID) + str(self.bodyType) + str(self.botNum) + ".nndf")

        #os.system("del brain" + str(self.solutionID) + ".nndf")

        pyrosim.Prepare_To_Simulate(self.robotID)
        self.Prepare_To_Sense()

        # self.Prepare_To_Act()

    def Prepare_To_Sense(self):

        self.sensors = {}

        for linkName in pyrosim.linkNamesToIndices:  # This is created after Prepare_To_Simulate
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self):
        for sensor in self.sensors:
            self.sensors[sensor].Get_Value()
            if sensor in {'TopSensor', 'BottomSensor',
                          'FrontTopSensor', 'FrontBottomSensor',
                          'BackTopSensor', 'BackBottomSensor',
                          'RightTopSensor', 'RightBottomSensor',
                          'LeftTopSensor', 'LeftBottomSensor'}:
                print("Robot: " + str(self.botNum) + ' link: ' + str(sensor) + ' Value: ' + str(self.sensors[sensor].Get_Value()))

    def Prepare_To_Act(self):

        self.motors = {}

        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

    def Think(self):
        self.nn.Update()
        #self.nn.Print()

    def Act(self):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName) * c.motorJointRange
                self.motors[jointName].Set_Value(self.robotID, desiredAngle)



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

