import random

import numpy as np
import pyrosim.pyrosim as pyrosim
import os
import time

import constants as c
import generate

class SOLUTION:
    def __init__(self, nextAvailableID, bodyType, numBots):
        self.myID = nextAvailableID
        self.bodyType = bodyType
        self.numBots = numBots
        #  self.weights = 2*np.random.rand(c.numSensorNeurons, c.numMotorNeurons)-1

    def Start_Simulation(self, DirectOrGUI):

        self.Create_World()
        self.Create_Body()
        # self.Create_Brain()
        print("here in solution start_simulation")
        os.system('START /B "" "C:\\Users\\Jared Krogsrud\\AppData\\Local\\Programs\\Python\\Python310\\python.exe" '
                  'simulate.py' + ' ' + DirectOrGUI + ' ' + str(self.myID) + ' ' + str(self.bodyType) + ' ' + str(self.numBots))
        print("here in solution start_simulation 2")

    def Wait_For_Simulation_To_End(self):

        while not os.path.exists("fitness" + str(self.myID) + ".txt"):
            time.sleep(0.01)

        file = open("fitness" + str(self.myID) + ".txt", "r")
        self.fitness = float(file.read())
        file.close()
        os.system("del fitness" + str(self.myID) + ".txt")

    def Mutate(self):
        randomRow = random.randint(0, c.numSensorNeurons - 1)
        randomColumn = random.randint(0, c.numMotorNeurons - 1)
        self.weights[randomRow, randomColumn] = 2 * random.random() - 1


    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")  # Creates file where world info will be stored

        # length = 2
        # width = 2
        # height = 2
        #
        # x = -4
        # y = 4
        # z = height / 2
        #
        # pyrosim.Send_Cube(name='box', pos=[x, y, z], size=[length, width, height])

        pyrosim.End()  # Close sdf file

    def Create_Body(self):

        for botNum in range(self.numBots):
            xCoord = 0 + botNum * 3
            yCoord = 0
            zCoord = 1
            generate.Generate_Body(self.bodyType, botNum, xCoord, yCoord, zCoord)

    def Create_Brain(self):
        pyrosim.Start_URDF("brain" + str(self.myID) + ".nndf")

        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")
        pyrosim.Send_Sensor_Neuron(name=3, linkName="LeftLeg")
        pyrosim.Send_Sensor_Neuron(name=4, linkName="RightLeg")
        pyrosim.Send_Sensor_Neuron(name=5, linkName="LowerBackLeg")
        pyrosim.Send_Sensor_Neuron(name=6, linkName="LowerFrontLeg")
        pyrosim.Send_Sensor_Neuron(name=7, linkName="LowerLeftLeg")
        pyrosim.Send_Sensor_Neuron(name=8, linkName="LowerRightLeg")

        pyrosim.Send_Motor_Neuron(name=9, jointName="Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name=10, jointName="Torso_FrontLeg")
        pyrosim.Send_Motor_Neuron(name=11, jointName="Torso_LeftLeg")
        pyrosim.Send_Motor_Neuron(name=12, jointName="Torso_RightLeg")
        pyrosim.Send_Motor_Neuron(name=13, jointName="BackLeg_LowerBackLeg")
        pyrosim.Send_Motor_Neuron(name=14, jointName="FrontLeg_LowerFrontLeg")
        pyrosim.Send_Motor_Neuron(name=15, jointName="LeftLeg_LowerLeftLeg")
        pyrosim.Send_Motor_Neuron(name=16, jointName="RightLeg_LowerRightLeg")

        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow,
                                     targetNeuronName=currentColumn+c.numSensorNeurons,
                                     weight=self.weights[currentRow][currentColumn])
        pyrosim.End()  # Close sdf file

    def Set_ID(self, newID):
        self.myID = newID