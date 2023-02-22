import random

import numpy as np
import pyrosim.pyrosim as pyrosim
import os
import time

import constants as c

class SOLUTION:
    def __init__(self, nextAvailableID):
        self.myID = nextAvailableID
        self.weights = 2*np.random.rand(c.numSensorNeurons, c.numMotorNeurons)-1

    def Start_Simulation(self, DirectOrGUI):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()

        os.system('START /B "" "C:\\Users\\Jared Krogsrud\\AppData\\Local\\Programs\\Python\\Python310\\python.exe" '
                  'simulate.py' + ' ' + DirectOrGUI + ' ' + str(self.myID))

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

        length = 2
        width = 2
        height = 2

        x = -4
        y = 4
        z = height / 2

        pyrosim.Send_Cube(name='box', pos=[x, y, z], size=[length, width, height])

        pyrosim.End()  # Close sdf file

    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")

        pyrosim.Send_Cube(name='Torso', pos=[0, 0, 1], size=[1, 1, 1])
        # Backlegs
        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute",
                           position=[0, -0.5, 1], jointAxis= "1 0 0")
        pyrosim.Send_Cube(name='BackLeg', pos=[0, -0.5, 0], size=[0.2, 1, 0.2])
        # BackLower
        pyrosim.Send_Joint(name="BackLeg_LowerBackLeg", parent="BackLeg", child="LowerBackLeg", type="revolute",
                           position=[0, -1, 0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name='LowerBackLeg', pos=[0, 0, -0.5], size=[0.2, 0.2, 1])

        # Frontlegs
        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute",
                           position=[0, 0.5, 1], jointAxis= "1 0 0")
        pyrosim.Send_Cube(name='FrontLeg', pos=[0, 0.5, 0], size=[0.2, 1, 0.2])
        # FrontLower
        pyrosim.Send_Joint(name="FrontLeg_LowerFrontLeg", parent="FrontLeg", child="LowerFrontLeg", type="revolute",
                           position=[0, 1, 0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name='LowerFrontLeg', pos=[0, 0, -0.5], size=[0.2, 0.2, 1])

        # Leftlegs
        pyrosim.Send_Joint(name="Torso_LeftLeg", parent="Torso", child="LeftLeg", type="revolute",
                           position=[-0.5, 0, 1], jointAxis="0 1 0")
        pyrosim.Send_Cube(name='LeftLeg', pos=[-0.5, 0, 0], size=[1, 0.2, 0.2])
        # LeftLower
        pyrosim.Send_Joint(name="LeftLeg_LowerLeftLeg", parent="LeftLeg", child="LowerLeftLeg", type="revolute",
                           position=[-1, 0, 0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name='LowerLeftLeg', pos=[0, 0, -0.5], size=[0.2, 0.2, 1])

        # Rightlegs
        pyrosim.Send_Joint(name="Torso_RightLeg", parent="Torso", child="RightLeg", type="revolute",
                           position=[0.5, 0, 1], jointAxis="0 1 0")
        pyrosim.Send_Cube(name='RightLeg', pos=[0.5, 0, 0], size=[1, 0.2, 0.2])
        #RightLower
        pyrosim.Send_Joint(name="RightLeg_LowerRightLeg", parent="RightLeg", child="LowerRightLeg", type="revolute",
                           position=[1, 0, 0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name='LowerRightLeg', pos=[0, 0, -0.5], size=[0.2, 0.2, 1])

        pyrosim.End()  # Close sdf file

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