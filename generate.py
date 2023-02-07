# this file will use pyrosim to create a link
# Store it in a file called world.sdf
# read and simulate this file

import pyrosim.pyrosim as pyrosim
import random


def create_world():
    pyrosim.Start_SDF("world.sdf")  # Creates file where world info will be stored

    length = 2
    width = 2
    height = 2

    x = -4
    y = 4
    z = height/2

    pyrosim.Send_Cube(name='box', pos=[x, y, z], size=[length, width, height])

    pyrosim.End()  # Close sdf file


def Generate_Body():
    pyrosim.Start_URDF("body.urdf")

    pyrosim.Send_Cube(name='Torso', pos=[1.5, 0, 1.5], size=[1, 1, 1])
    pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute",
                       position=[1, 0, 1])
    pyrosim.Send_Cube(name='BackLeg', pos=[-0.5, 0, -0.5], size=[1, 1, 1])
    pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute",
                       position=[2, 0, 1])
    pyrosim.Send_Cube(name='FrontLeg', pos=[0.5, 0, -0.5], size=[1, 1, 1])

    pyrosim.End()  # Close sdf file


def Generate_Brain():
    pyrosim.Start_URDF("brain.nndf")

    pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
    pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
    pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")

    pyrosim.Send_Motor_Neuron(name=3, jointName="Torso_BackLeg")
    pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_FrontLeg")

    for sensor_name in range(3):
        for motor in range(3, 5):
            pyrosim.Send_Synapse(sourceNeuronName=sensor_name, targetNeuronName=motor, weight=random.random() % 1)
    pyrosim.End()  # Close sdf file



create_world()
Generate_Body()
Generate_Brain()