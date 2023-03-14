# This file is going to be adapted to be able to generate the type of body at a specific location
# it will be called by solution to create the body when needed

import pyrosim.pyrosim as pyrosim
import random
import time
import constants as c
import numpy as np


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
        torsoHeight = .20
        torsoSensorHeight = .15
        torsoSensorSize = .75

        print("body_" + str(bodyType) + str(botNum) + ".urdf created")
        pyrosim.Start_URDF("body_" + str(bodyType) + str(botNum) + ".urdf")

        pyrosim.Send_Cube(name='Torso', pos=[xCoord, yCoord, zCoord], size=[1, 1, torsoHeight])
        # Top Sensor
        pyrosim.Send_Joint(name='Torso_TopSensor', parent="Torso", child="TopSensor",
                           type="fixed", position=[xCoord, yCoord, zCoord + (torsoHeight / 2)], jointAxis="1 0 0")
        pyrosim.Send_Cube(name='TopSensor', pos=[0, 0, 0], size=[torsoSensorSize, torsoSensorSize, torsoSensorHeight])
        # Bottom Sensor
        pyrosim.Send_Joint(name='Torso_BottomSensor', parent="Torso", child="BottomSensor",
                           type="fixed", position=[xCoord, yCoord, zCoord - (torsoHeight / 2)], jointAxis="1 0 0")
        pyrosim.Send_Cube(name='BottomSensor', pos=[0, 0, 0], size=[torsoSensorSize, torsoSensorSize, torsoSensorHeight])

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
        pyrosim.Send_Joint(name='LeftFlap_LeftBottomSensor', parent="LeftFlap", child="LeftBottomSensor",
                           type="fixed", position=[-bottomFlapSensorOffset, 0, -.0625], jointAxis="1 0 0")
        pyrosim.Send_Cube(name='LeftBottomSensor', pos=[0, 0, 0], size=[.25, .25, 0.125])

        # UR LEG
        # Rotator Cuff
        pyrosim.Send_Joint(name='Torso_URRotate', parent="Torso", child="URRotate",
                           type="revolute", position=[xCoord - 0.5, yCoord - 0.5, zCoord], jointAxis="0 0 1")
        pyrosim.Send_Cube(name='URRotate', pos=[0, 0, 0], size=[.2, .2, .2])
        # Top Leg
        pyrosim.Send_Joint(name='URRotate_URTopLeg', parent="URRotate", child="URTopLeg",
                           type="revolute", position=[0, 0, 0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name='URTopLeg', pos=[-.6, 0, 0], size=[1.2, .2, .2])
        # Bottom Leg
        pyrosim.Send_Joint(name='URTopLeg_URBottomLeg', parent="URTopLeg", child="URBottomLeg",
                           type="revolute", position=[-1.2, 0, 0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name='URBottomLeg', pos=[-0.5, 0, 0], size=[1, .2, .2])

        # UL LEG
        # Rotator Cuff
        pyrosim.Send_Joint(name='Torso_ULRotate', parent="Torso", child="ULRotate",
                           type="revolute", position=[xCoord - 0.5, yCoord + 0.5, zCoord], jointAxis="0 0 1")
        pyrosim.Send_Cube(name='ULRotate', pos=[0, 0, 0], size=[.2, .2, .2])
        # Top Leg
        pyrosim.Send_Joint(name='ULRotate_ULTopLeg', parent="ULRotate", child="ULTopLeg",
                           type="revolute", position=[0, 0, 0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name='ULTopLeg', pos=[-.6, 0, 0], size=[1.2, .2, .2])
        # Bottom Leg
        pyrosim.Send_Joint(name='ULTopLeg_ULBottomLeg', parent="ULTopLeg", child="ULBottomLeg",
                           type="revolute", position=[-1.2, 0, 0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name='ULBottomLeg', pos=[-0.5, 0, 0], size=[1, .2, .2])

        # BR LEG
        # Rotator Cuff
        pyrosim.Send_Joint(name='Torso_BRRotate', parent="Torso", child="BRRotate",
                           type="revolute", position=[xCoord + 0.5, yCoord + 0.5, zCoord], jointAxis="0 0 1")
        pyrosim.Send_Cube(name='BRRotate', pos=[0, 0, 0], size=[.2, .2, .2])
        # Top Leg
        pyrosim.Send_Joint(name='BRRotate_BRTopLeg', parent="BRRotate", child="BRTopLeg",
                           type="revolute", position=[0, 0, 0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name='BRTopLeg', pos=[.6, 0, 0], size=[1.2, .2, .2])
        # Bottom Leg
        pyrosim.Send_Joint(name='BRTopLeg_BRBottomLeg', parent="BRTopLeg", child="BRBottomLeg",
                           type="revolute", position=[1.2, 0, 0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name='BRBottomLeg', pos=[0.5, 0, 0], size=[1, .2, .2])

        # BL LEG
        # Rotator Cuff
        pyrosim.Send_Joint(name='Torso_BLRotate', parent="Torso", child="BLRotate",
                           type="revolute", position=[xCoord + 0.5, yCoord - 0.5, zCoord], jointAxis="0 0 1")
        pyrosim.Send_Cube(name='BLRotate', pos=[0, 0, 0], size=[.2, .2, .2])
        # Top Leg
        pyrosim.Send_Joint(name='BLRotate_BLTopLeg', parent="BLRotate", child="BLTopLeg",
                           type="revolute", position=[0, 0, 0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name='BLTopLeg', pos=[.6, 0, 0], size=[1.2, .2, .2])
        # Bottom Leg
        pyrosim.Send_Joint(name='BLTopLeg_BLBottomLeg', parent="BLTopLeg", child="BLBottomLeg",
                           type="revolute", position=[1.2, 0, 0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name='BLBottomLeg', pos=[0.5, 0, 0], size=[1, .2, .2])

        pyrosim.End()  # Close sdf file


def Generate_Brain(solutionID, bodyType, botNum):
    pyrosim.Start_URDF("brain_" + str(solutionID) + str(bodyType) + str(botNum) + ".nndf")

    # Sensors for Cubes
    # Torso Sensors
    pyrosim.Send_Sensor_Neuron(name=39*botNum + 0, linkName='Torso')
    pyrosim.Send_Sensor_Neuron(name=39*botNum + 1, linkName='TopSensor')
    pyrosim.Send_Sensor_Neuron(name=39*botNum + 2, linkName='BottomSensor')

    # Flaps
    pyrosim.Send_Sensor_Neuron(name=39*botNum + 3, linkName='FrontFlap')
    pyrosim.Send_Sensor_Neuron(name=39*botNum + 4, linkName='FrontTopSensor')
    pyrosim.Send_Sensor_Neuron(name=39*botNum + 5, linkName='FrontBottomSensor')

    pyrosim.Send_Sensor_Neuron(name=39*botNum + 6, linkName='BackFlap')
    pyrosim.Send_Sensor_Neuron(name=39*botNum + 7, linkName='BackTopSensor')
    pyrosim.Send_Sensor_Neuron(name=39*botNum + 8, linkName='BackBottomSensor')

    pyrosim.Send_Sensor_Neuron(name=39*botNum + 9, linkName='RightFlap')
    pyrosim.Send_Sensor_Neuron(name=39*botNum + 10, linkName='RightTopSensor')
    pyrosim.Send_Sensor_Neuron(name=39*botNum + 11, linkName='RightBottomSensor')

    pyrosim.Send_Sensor_Neuron(name=39*botNum + 12, linkName='LeftFlap')
    pyrosim.Send_Sensor_Neuron(name=39*botNum + 13, linkName='LeftTopSensor')
    pyrosim.Send_Sensor_Neuron(name=39*botNum + 14, linkName='LeftBottomSensor')

    # Legs
    pyrosim.Send_Sensor_Neuron(name=39*botNum + 15, linkName='URTopLeg')
    pyrosim.Send_Sensor_Neuron(name=39*botNum + 16, linkName='URBottomLeg')

    pyrosim.Send_Sensor_Neuron(name=39*botNum + 17, linkName='ULTopLeg')
    pyrosim.Send_Sensor_Neuron(name=39*botNum + 18, linkName='ULBottomLeg')

    pyrosim.Send_Sensor_Neuron(name=39*botNum + 19, linkName='BRTopLeg')
    pyrosim.Send_Sensor_Neuron(name=39*botNum + 20, linkName='BRBottomLeg')

    pyrosim.Send_Sensor_Neuron(name=39*botNum + 21, linkName='BLTopLeg')
    pyrosim.Send_Sensor_Neuron(name=39*botNum + 22, linkName='BLBottomLeg')

    ### MOTORS ###

    ## Flaps ##
    pyrosim.Send_Motor_Neuron(name=39*botNum + 23, jointName='Torso_FrontFlap')
    pyrosim.Send_Motor_Neuron(name=39*botNum + 24, jointName='Torso_BackFlap')
    pyrosim.Send_Motor_Neuron(name=39*botNum + 25, jointName='Torso_RightFlap')
    pyrosim.Send_Motor_Neuron(name=39*botNum + 26, jointName='Torso_LeftFlap')

    ## Legs ##
    # Upper Right #
    pyrosim.Send_Motor_Neuron(name=39*botNum + 27, jointName='Torso_URRotate')
    pyrosim.Send_Motor_Neuron(name=39*botNum + 28, jointName='URRotate_URTopLeg')
    pyrosim.Send_Motor_Neuron(name=39*botNum + 29, jointName='URTopLeg_URBottomLeg')

    # Upper Left #
    pyrosim.Send_Motor_Neuron(name=39*botNum + 30, jointName='Torso_ULRotate')
    pyrosim.Send_Motor_Neuron(name=39*botNum + 31, jointName='ULRotate_ULTopLeg')
    pyrosim.Send_Motor_Neuron(name=39*botNum + 32, jointName='ULTopLeg_ULBottomLeg')

    # Back Right #
    pyrosim.Send_Motor_Neuron(name=39*botNum + 33, jointName='Torso_BRRotate')
    pyrosim.Send_Motor_Neuron(name=39*botNum + 34, jointName='BRRotate_BRTopLeg')
    pyrosim.Send_Motor_Neuron(name=39*botNum + 35, jointName='BRTopLeg_BRBottomLeg')

    # Back Left #
    pyrosim.Send_Motor_Neuron(name=39*botNum + 36, jointName='Torso_BLRotate')
    pyrosim.Send_Motor_Neuron(name=39*botNum + 37, jointName='BLRotate_BLTopLeg')
    pyrosim.Send_Motor_Neuron(name=39*botNum + 38, jointName='BLTopLeg_BLBottomLeg')

    pyrosim.End()

    # for sensor_name 23*botNum + in range(3):
    #     for motor in range(3, 5):
    #         pyrosim.Send_Synapse(sourceNeuronName=sensor_name, targetNeuronName=motor, weight=random.random() % 1)
    # pyrosim.End()  # Close sdf file

def Generate_Oscillation(bodyType, jointName):

    amplitude = c.FRONT_AMP
    frequency = c.FRONT_FREQ
    offset = c.FRONT_PHASE

    x = np.linspace(start=0 - offset, stop=2 * np.pi - offset, num=c.FRAMES) * frequency

    motorValues = np.sin(x)*amplitude

    return motorValues

    # if bodyType == 'A':
    #     match jointName:
    #         case '':
    #             pass
    #         case _:
    #             pass