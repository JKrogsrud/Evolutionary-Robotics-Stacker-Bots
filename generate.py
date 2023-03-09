# This file is going to be adapted to be able to generate the type of body at a specific location
# it will be called by solution to create the body when needed

import pyrosim.pyrosim as pyrosim
import random
import time


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


def Generate_Body(bodyType, botNum, xCoord, yCoord, zCoord):
    if bodyType == "A":

        topFlapSensorOffset = .45
        bottomFlapSensorOffset = .55
        torsoHeight = .25

        print("body_" + str(bodyType) + str(botNum) + ".urdf created")
        pyrosim.Start_URDF("body_" + str(bodyType) + str(botNum) + ".urdf")

        # Torso ---- OG: [0, 0, 1]
        pyrosim.Send_Cube(name='Torso', pos=[xCoord, yCoord, zCoord], size=[1, 1, torsoHeight])
        # Top Sensor
        pyrosim.Send_Joint(name='Torso_TopSensor', parent="Torso", child="TopSensor",
                           type="fixed", position=[xCoord, yCoord, zCoord + (torsoHeight / 2)], jointAxis="1 0 0")
        pyrosim.Send_Cube(name='TopSensor', pos=[0, 0, 0], size=[.5, .5, torsoHeight/3.5])
        # Bottom Sensor
        pyrosim.Send_Joint(name='Torso_BottomSensor', parent="Torso", child="BottomSensor",
                           type="fixed", position=[xCoord, yCoord, zCoord - (torsoHeight / 2)], jointAxis="1 0 0")
        pyrosim.Send_Cube(name='BottomSensor', pos=[0, 0, 0], size=[.5, .5, torsoHeight/3.5])

        # FRONTFLAP
        pyrosim.Send_Joint(name='Torso_FrontFlap', parent="Torso", child="FrontFlap",
                           type="revolute", position=[xCoord, yCoord + 0.5, zCoord], jointAxis="1 0 0")
        pyrosim.Send_Cube(name='FrontFlap', pos=[0, 0.75 / 2, 0], size=[.5, .75, 0.125])
        # Top Sensor
        pyrosim.Send_Joint(name='FrontFlap_FrontTopSensor', parent="FrontFlap", child="FrontTopSensor",
                           type="fixed", position=[0, topFlapSensorOffset, .0625], jointAxis="1 0 0")
        pyrosim.Send_Cube(name='FrontTopSensor', pos=[0, 0, 0], size=[.25, .25, 0.125])
        # Bottom Sensor
        pyrosim.Send_Joint(name='FrontFlap_FrontBottomSensor', parent="FrontFlap", child="FrontBottomSensor",
                           type="fixed", position=[0, bottomFlapSensorOffset, -.0625], jointAxis="1 0 0")
        pyrosim.Send_Cube(name='FrontBottomSensor', pos=[0, 0, 0], size=[.25, .25, 0.125])

        # BACKFLAP
        pyrosim.Send_Joint(name='Torso_BackFlap', parent="Torso", child="BackFlap",
                           type="revolute", position=[xCoord, yCoord - 0.5, zCoord], jointAxis="1 0 0")
        pyrosim.Send_Cube(name='BackFlap', pos=[0, -0.75 / 2, 0], size=[.5, .75, 0.125])
        # Top Sensor
        pyrosim.Send_Joint(name='BackFlap_BackTopSensor', parent="BackFlap", child="BackTopSensor",
                           type="fixed", position=[0, -topFlapSensorOffset, .0625], jointAxis="1 0 0")
        pyrosim.Send_Cube(name='BackTopSensor', pos=[0, 0, 0], size=[.25, .25, 0.125])
        # Bottom Sensor
        pyrosim.Send_Joint(name='BackFlap_BackBottomSensor', parent="BackFlap", child="BackBottomSensor",
                           type="fixed", position=[0, -bottomFlapSensorOffset, -.0625], jointAxis="1 0 0")
        pyrosim.Send_Cube(name='BackBottomSensor', pos=[0, 0, 0], size=[.25, .25, 0.125])

        # RIGHTFLAP
        pyrosim.Send_Joint(name='Torso_RightFlap', parent="Torso", child="RightFlap",
                           type="revolute", position=[xCoord + 0.5, yCoord, zCoord], jointAxis="0 1 0")
        pyrosim.Send_Cube(name='RightFlap', pos=[0.75 / 2, 0, 0], size=[.75, .5, 0.125])
        # Top Sensor
        pyrosim.Send_Joint(name='RightFlap_RightTopSensor', parent="RightFlap", child="RightTopSensor",
                           type="fixed", position=[topFlapSensorOffset, 0, .0625], jointAxis="1 0 0")
        pyrosim.Send_Cube(name='RightTopSensor', pos=[0, 0, 0], size=[.25, .25, 0.125])
        # Bottom Sensor
        pyrosim.Send_Joint(name='RightFlap_RightBottomSensor', parent="RightFlap", child="RightBottomSensor",
                           type="fixed", position=[bottomFlapSensorOffset, 0, -.0625], jointAxis="1 0 0")
        pyrosim.Send_Cube(name='RightBottomSensor', pos=[0, 0, 0], size=[.25, .25, 0.125])

        # LEFTFLAP
        pyrosim.Send_Joint(name='Torso_LeftFlap', parent="Torso", child="LeftFlap",
                           type="revolute", position=[xCoord - 0.5, yCoord, zCoord], jointAxis="0 1 0")
        pyrosim.Send_Cube(name='LeftFlap', pos=[-0.75 / 2, 0, 0], size=[.75, .5, 0.125])
        # Top Sensor
        pyrosim.Send_Joint(name='LeftFlap_LeftTopSensor', parent="LeftFlap", child="LeftTopSensor",
                           type="fixed", position=[-topFlapSensorOffset, 0, .0625], jointAxis="1 0 0")
        pyrosim.Send_Cube(name='LeftTopSensor', pos=[0, 0, 0], size=[.25, .25, 0.125])
        # Bottom Sensor
        pyrosim.Send_Joint(name='LeftFlap_RightBottomSensor', parent="LeftFlap", child="LeftBottomSensor",
                           type="fixed", position=[-bottomFlapSensorOffset, 0, -.0625], jointAxis="1 0 0")
        pyrosim.Send_Cube(name='LeftBottomSensor', pos=[0, 0, 0], size=[.25, .25, 0.125])

        # UR LEG
        # Rotator Cuff
        pyrosim.Send_Joint(name='Torso_UR_Rotate', parent="Torso", child="UR_Rotate",
                           type="revolute", position=[xCoord - 0.5, yCoord - 0.5, zCoord], jointAxis="0 0 1")
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
                           type="revolute", position=[xCoord - 0.5, yCoord + 0.5, zCoord], jointAxis="0 0 1")
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
                           type="revolute", position=[xCoord + 0.5, yCoord + 0.5, zCoord], jointAxis="0 0 1")
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
                           type="revolute", position=[xCoord + 0.5, yCoord - 0.5, zCoord], jointAxis="0 0 1")
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

