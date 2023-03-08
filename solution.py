import random

import numpy as np
import pyrosim.pyrosim as pyrosim
import os
import time

import constants as c
import generate

class SOLUTION:
    def __init__(self, nextAvailableID, bodyType):
        self.myID = nextAvailableID
        self.bodyType = bodyType
        #  self.weights = 2*np.random.rand(c.numSensorNeurons, c.numMotorNeurons)-1

    def Start_Simulation(self, DirectOrGUI):

        self.Create_World()
        self.Create_Body()
        # self.Create_Brain()

        os.system('START /B "" "C:\\Users\\Jared Krogsrud\\AppData\\Local\\Programs\\Python\\Python310\\python.exe" '
                  'simulate.py' + ' ' + DirectOrGUI + ' ' + str(self.myID) + ' ' + str(self.bodyType))

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

        generate.Generate_Body(self.bodyType, self.myID, )

        if self.bodyType == "A_1":
            pyrosim.Start_URDF("body_" + self.bodyType + ".urdf")

            # Torso
            pyrosim.Send_Cube(name='Torso', pos=[0, 0, 1], size=[1, 1, 0.5])
            # Top Sensor
            pyrosim.Send_Joint(name='Torso_TopSensor', parent="Torso", child="TopSensor",
                               type="fixed", position=[0, 0, 1.25], jointAxis="1 0 0")
            pyrosim.Send_Cube(name='TopSensor', pos=[0, 0, 0], size=[.5, .5, 0.125])
            # Bottom Sensor
            pyrosim.Send_Joint(name='Torso_BottomSensor', parent="Torso", child="BottomSensor",
                               type="fixed", position=[0, 0, .75], jointAxis="1 0 0")
            pyrosim.Send_Cube(name='BottomSensor', pos=[0, 0, 0], size=[.5, .5, 0.125])

            # FRONTFLAP
            pyrosim.Send_Joint(name='Torso_FrontFlap', parent="Torso", child="FrontFlap",
                               type="revolute", position=[0, 0.5, 1], jointAxis="1 0 0")
            pyrosim.Send_Cube(name='FrontFlap', pos=[0, 0.75/2, 0], size=[.5, .75, 0.125])
            # Top Sensor
            pyrosim.Send_Joint(name='FrontFlap_FrontTopSensor', parent="FrontFlap", child="FrontTopSensor",
                               type="fixed", position=[0, 0.5, .0625], jointAxis="1 0 0")
            pyrosim.Send_Cube(name='FrontTopSensor', pos=[0, 0, 0], size=[.25, .25, 0.125])
            # Bottom Sensor
            pyrosim.Send_Joint(name='FrontFlap_FrontBottomSensor', parent="FrontFlap", child="FrontBottomSensor",
                               type="fixed", position=[0, 0.5, -.0625], jointAxis="1 0 0")
            pyrosim.Send_Cube(name='FrontBottomSensor', pos=[0, 0, 0], size=[.25, .25, 0.125])

            # BACKFLAP
            pyrosim.Send_Joint(name='Torso_BackFlap', parent="Torso", child="BackFlap",
                               type="revolute", position=[0, -0.5, 1], jointAxis="1 0 0")
            pyrosim.Send_Cube(name='BackFlap', pos=[0, -0.75/2, 0], size=[.5, .75, 0.125])
            # Top Sensor
            pyrosim.Send_Joint(name='BackFlap_BackTopSensor', parent="BackFlap", child="BackTopSensor",
                               type="fixed", position=[0, -0.5, .0625], jointAxis="1 0 0")
            pyrosim.Send_Cube(name='BackTopSensor', pos=[0, 0, 0], size=[.25, .25, 0.125])
            # Bottom Sensor
            pyrosim.Send_Joint(name='BackFlap_BackBottomSensor', parent="BackFlap", child="BackBottomSensor",
                               type="fixed", position=[0, -0.5, -.0625], jointAxis="1 0 0")
            pyrosim.Send_Cube(name='BackBottomSensor', pos=[0, 0, 0], size=[.25, .25, 0.125])

            # RIGHTFLAP
            pyrosim.Send_Joint(name='Torso_RightFlap', parent="Torso", child="RightFlap",
                               type="revolute", position=[0.5, 0, 1], jointAxis="0 1 0")
            pyrosim.Send_Cube(name='RightFlap', pos=[0.75/2, 0, 0], size=[.75, .5, 0.125])
            # Top Sensor
            pyrosim.Send_Joint(name='RightFlap_RightTopSensor', parent="RightFlap", child="RightTopSensor",
                               type="fixed", position=[0.5, 0, .0625], jointAxis="1 0 0")
            pyrosim.Send_Cube(name='RightTopSensor', pos=[0, 0, 0], size=[.25, .25, 0.125])
            # Bottom Sensor
            pyrosim.Send_Joint(name='RightFlap_RightBottomSensor', parent="RightFlap", child="RightBottomSensor",
                               type="fixed", position=[0.5, 0, -.0625], jointAxis="1 0 0")
            pyrosim.Send_Cube(name='RightBottomSensor', pos=[0, 0, 0], size=[.25, .25, 0.125])

            # LEFTFLAP
            pyrosim.Send_Joint(name='Torso_LeftFlap', parent="Torso", child="LeftFlap",
                               type="revolute", position=[-0.5, 0, 1], jointAxis="0 1 0")
            pyrosim.Send_Cube(name='LeftFlap', pos=[-0.75/2, 0, 0], size=[.75, .5, 0.125])
            # Top Sensor
            pyrosim.Send_Joint(name='LeftFlap_LeftTopSensor', parent="LeftFlap", child="LeftTopSensor",
                               type="fixed", position=[-0.5, 0, .0625], jointAxis="1 0 0")
            pyrosim.Send_Cube(name='LeftTopSensor', pos=[0, 0, 0], size=[.25, .25, 0.125])
            # Bottom Sensor
            pyrosim.Send_Joint(name='LeftFlap_RightBottomSensor', parent="LeftFlap", child="LeftBottomSensor",
                               type="fixed", position=[-0.5, 0, -.0625], jointAxis="1 0 0")
            pyrosim.Send_Cube(name='LeftBottomSensor', pos=[0, 0, 0], size=[.25, .25, 0.125])

            # UR LEG
            # Rotator Cuff
            pyrosim.Send_Joint(name='Torso_UR_Rotate', parent="Torso", child="UR_Rotate",
                               type="revolute", position=[-0.5, -0.5, 1], jointAxis="0 0 1")
            pyrosim.Send_Cube(name='UR_Rotate', pos=[0, 0, 0], size=[.2, .2, .2])
            # Top Leg
            pyrosim.Send_Joint(name='UR_Rotate_UR_Top_Leg', parent="UR_Rotate", child="UR_Top_Leg",
                               type="revolute", position=[0, 0, 0], jointAxis="0 1 0")
            pyrosim.Send_Cube(name='UR_Top_Leg', pos=[-.6, 0, 0], size=[1.2, .2, .2])
            # Bottom Leg
            pyrosim.Send_Joint(name='UR_Top_Leg_UR_Bottom_Leg', parent="UR_Top_Leg", child="UR_Bottom_Leg",
                               type="revolute", position=[-1.2, 0, 0], jointAxis="0 1 0")
            pyrosim.Send_Cube(name='UR_Bottom_Leg', pos=[-0.5, 0, 0], size=[1, .2, .2])

            # UL LEG
            # Rotator Cuff
            pyrosim.Send_Joint(name='Torso_UL_Rotate', parent="Torso", child="UL_Rotate",
                               type="revolute", position=[-0.5, 0.5, 1], jointAxis="0 0 1")
            pyrosim.Send_Cube(name='UL_Rotate', pos=[0, 0, 0], size=[.2, .2, .2])
            # Top Leg
            pyrosim.Send_Joint(name='UL_Rotate_UL_Top_Leg', parent="UL_Rotate", child="UL_Top_Leg",
                               type="revolute", position=[0, 0, 0], jointAxis="0 1 0")
            pyrosim.Send_Cube(name='UL_Top_Leg', pos=[-.6, 0, 0], size=[1.2, .2, .2])
            # Bottom Leg
            pyrosim.Send_Joint(name='UL_Top_Leg_UL_Bottom_Leg', parent="UL_Top_Leg", child="UL_Bottom_Leg",
                               type="revolute", position=[-1.2, 0, 0], jointAxis="0 1 0")
            pyrosim.Send_Cube(name='UL_Bottom_Leg', pos=[-0.5, 0, 0], size=[1, .2, .2])

            # BR LEG
            # Rotator Cuff
            pyrosim.Send_Joint(name='Torso_BR_Rotate', parent="Torso", child="BR_Rotate",
                               type="revolute", position=[0.5, 0.5, 1], jointAxis="0 0 1")
            pyrosim.Send_Cube(name='BR_Rotate', pos=[0, 0, 0], size=[.2, .2, .2])
            # Top Leg
            pyrosim.Send_Joint(name='BR_Rotate_BR_Top_Leg', parent="BR_Rotate", child="BR_Top_Leg",
                               type="revolute", position=[0, 0, 0], jointAxis="0 1 0")
            pyrosim.Send_Cube(name='BR_Top_Leg', pos=[.6, 0, 0], size=[1.2, .2, .2])
            # Bottom Leg
            pyrosim.Send_Joint(name='BR_Top_Leg_BR_Bottom_Leg', parent="BR_Top_Leg", child="BR_Bottom_Leg",
                               type="revolute", position=[1.2, 0, 0], jointAxis="0 1 0")
            pyrosim.Send_Cube(name='BR_Bottom_Leg', pos=[0.5, 0, 0], size=[1, .2, .2])

            # BL LEG
            # Rotator Cuff
            pyrosim.Send_Joint(name='Torso_BL_Rotate', parent="Torso", child="BL_Rotate",
                               type="revolute", position=[0.5, -0.5, 1], jointAxis="0 0 1")
            pyrosim.Send_Cube(name='BL_Rotate', pos=[0, 0, 0], size=[.2, .2, .2])
            # Top Leg
            pyrosim.Send_Joint(name='BL_Rotate_BL_Top_Leg', parent="BL_Rotate", child="BL_Top_Leg",
                               type="revolute", position=[0, 0, 0], jointAxis="0 1 0")
            pyrosim.Send_Cube(name='BL_Top_Leg', pos=[.6, 0, 0], size=[1.2, .2, .2])
            # Bottom Leg
            pyrosim.Send_Joint(name='BL_Top_Leg_BL_Bottom_Leg', parent="BL_Top_Leg", child="BL_Bottom_Leg",
                               type="revolute", position=[1.2, 0, 0], jointAxis="0 1 0")
            pyrosim.Send_Cube(name='BL_Bottom_Leg', pos=[0.5, 0, 0], size=[1, .2, .2])

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