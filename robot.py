import pybullet as p
import pyrosim.pyrosim as pyrosim
import constants as c
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os

from sensor import SENSOR
from motor import MOTOR

class ROBOT:

    def __init__(self, solutionID):
        self.solutionID = solutionID
        self.robotID = p.loadURDF("body.urdf")
        self.nn = NEURAL_NETWORK("brain" + str(self.solutionID) + ".nndf")

        os.system("del brain" + str(self.solutionID) + ".nndf")

        pyrosim.Prepare_To_Simulate(self.robotID)

        self.Prepare_To_Sense()
        self.Prepare_To_Act()

    def Prepare_To_Sense(self):

        self.sensors = {}

        for linkName in pyrosim.linkNamesToIndices:  # This is created after Prepare_To_Simulate
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self):
        for sensor in self.sensors:
            self.sensors[sensor].Get_Value()

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
                desiredAngle = self.nn.Get_Value_Of(neuronName)
                self.motors[jointName].Set_Value(self.robotID, desiredAngle)



    def Save_Values(self):

        for sensor in self.sensors:
            self.sensors[sensor].Save_Values()
        for motor in self.motors:
            self.motors[motor].Save_Values()


    def Get_Fitness(self):
        stateOfLinkZero = p.getLinkState(self.robotID, 0)
        positionOfLinkZero = stateOfLinkZero[0]
        xCoordinateLinkZero = positionOfLinkZero[0]

        f = open("tmp" + str(self.solutionID) + ".txt", "w")
        f.write(str(xCoordinateLinkZero))
        f.close()

        os.rename("tmp"+ str(self.solutionID) + ".txt", "fitness" + str(self.solutionID) + ".txt")

