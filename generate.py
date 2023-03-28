# This file is going to be adapted to be able to generate the type of body at a specific location
# it will be called by solution to create the body when needed

import pyrosim.pyrosim as pyrosim
import random
import time
import constants as c
import numpy as np


# Outdated
def create_world():
    pyrosim.Start_SDF('world.sdf')  # Creates file where world info will be stored

    length = 2
    width = 2
    height = 2

    x = -4
    y = 4
    z = height/2

    pyrosim.Send_Cube(name='box', pos=[x, y, z], size=[length, width, height])

    pyrosim.End()  # Close sdf file


def Generate_Body(bodyType, botNum, xCoord, yCoord, zCoord, startingIndex, botName):
    if bodyType == 'A':

        # print('body_' + str(bodyType) + str(botNum) + '.urdf created')
        pyrosim.Start_URDF('body_' + str(bodyType) + str(botNum) + '.urdf', startingIndex, botName)

        pyrosim.Send_Cube(name=str(botNum) + 'Torso', pos=[xCoord, yCoord, zCoord], size=[1, 1, c.torsoHeight])
        # Top Sensor
        pyrosim.Send_Joint(name=str(botNum) + 'Torso_' + str(botNum) + 'TopSensor', parent=str(botNum) + 'Torso', child=str(botNum) + 'TopSensor',
                           type='fixed', position=[xCoord, yCoord, zCoord + (c.torsoHeight / 2)], jointAxis="1 0 0")
        pyrosim.Send_Cube(name=str(botNum) + 'TopSensor', pos=[0, 0, 0], size=[c.torsoSensorSize, c.torsoSensorSize, c.torsoSensorHeight])
        # Bottom Sensor
        pyrosim.Send_Joint(name=str(botNum) + 'Torso_' + str(botNum) + 'BottomSensor', parent=str(botNum) + 'Torso', child=str(botNum) + 'BottomSensor',
                           type="fixed", position=[xCoord, yCoord, zCoord - (c.torsoHeight / 2)], jointAxis="1 0 0")
        pyrosim.Send_Cube(name=str(botNum) + 'BottomSensor', pos=[0, 0, 0], size=[c.torsoSensorSize, c.torsoSensorSize, c.torsoSensorHeight])

        # FRONTFLAP
        pyrosim.Send_Joint(name=str(botNum) + 'Torso_' + str(botNum) + 'FrontFlap', parent=str(botNum) + 'Torso', child=str(botNum) + 'FrontFlap',
                           type='revolute', position=[xCoord, yCoord + 0.5, zCoord], jointAxis='1 0 0')
        pyrosim.Send_Cube(name=str(botNum) + 'FrontFlap', pos=[0, 0.75 / 2, 0], size=[.5, .75, 0.125])
        # Top Sensor
        pyrosim.Send_Joint(name=str(botNum) + 'FrontFlap_' + str(botNum) + 'FrontTopSensor', parent=str(botNum) + 'FrontFlap', child=str(botNum) + 'FrontTopSensor',
                           type='fixed', position=[0, c.topFlapSensorOffset, .0625], jointAxis='1 0 0')
        pyrosim.Send_Cube(name=str(botNum) + 'FrontTopSensor', pos=[0, 0, 0], size=[.25, .25, 0.125])
        # Bottom Sensor
        pyrosim.Send_Joint(name=str(botNum) + 'FrontFlap_' + str(botNum) + 'FrontBottomSensor', parent=str(botNum) + 'FrontFlap', child=str(botNum) + 'FrontBottomSensor',
                           type='fixed', position=[0, c.bottomFlapSensorOffset, -.0625], jointAxis='1 0 0')
        pyrosim.Send_Cube(name=str(botNum) + 'FrontBottomSensor', pos=[0, 0, 0], size=[.25, .25, 0.125])

        # BACKFLAP
        pyrosim.Send_Joint(name=str(botNum) + 'Torso_'+ str(botNum) + 'BackFlap', parent=str(botNum) + 'Torso', child=str(botNum) + 'BackFlap',
                           type='revolute', position=[xCoord, yCoord - 0.5, zCoord], jointAxis='1 0 0')
        pyrosim.Send_Cube(name=str(botNum) + 'BackFlap', pos=[0, -0.75 / 2, 0], size=[.5, .75, 0.125])
        # Top Sensor
        pyrosim.Send_Joint(name=str(botNum) + 'BackFlap_' + str(botNum) + 'BackTopSensor', parent=str(botNum) + 'BackFlap', child=str(botNum) + 'BackTopSensor',
                           type='fixed', position=[0, -c.topFlapSensorOffset, .0625], jointAxis='1 0 0')
        pyrosim.Send_Cube(name=str(botNum) + 'BackTopSensor', pos=[0, 0, 0], size=[.25, .25, 0.125])
        # Bottom Sensor
        pyrosim.Send_Joint(name=str(botNum) + 'BackFlap_' + str(botNum) + 'BackBottomSensor', parent=str(botNum) + 'BackFlap', child=str(botNum) + 'BackBottomSensor',
                           type='fixed', position=[0, -c.bottomFlapSensorOffset, -.0625], jointAxis='1 0 0')
        pyrosim.Send_Cube(name=str(botNum) + 'BackBottomSensor', pos=[0, 0, 0], size=[.25, .25, 0.125])

        # RIGHTFLAP
        pyrosim.Send_Joint(name=str(botNum) + 'Torso_' + str(botNum) + 'RightFlap', parent=str(botNum) + 'Torso', child=str(botNum) + 'RightFlap',
                           type='revolute', position=[xCoord + 0.5, yCoord, zCoord], jointAxis='0 1 0')
        pyrosim.Send_Cube(name=str(botNum) + 'RightFlap', pos=[0.75 / 2, 0, 0], size=[.75, .5, 0.125])
        # Top Sensor
        pyrosim.Send_Joint(name=str(botNum) + 'RightFlap_'+ str(botNum) + 'RightTopSensor', parent=str(botNum) + 'RightFlap', child=str(botNum) + 'RightTopSensor',
                           type='fixed', position=[c.topFlapSensorOffset, 0, .0625], jointAxis='1 0 0')
        pyrosim.Send_Cube(name=str(botNum) + 'RightTopSensor', pos=[0, 0, 0], size=[.25, .25, 0.125])
        # Bottom Sensor
        pyrosim.Send_Joint(name=str(botNum) + 'RightFlap_'+ str(botNum) + 'RightBottomSensor', parent=str(botNum) + 'RightFlap', child=str(botNum) + 'RightBottomSensor',
                           type='fixed', position=[c.bottomFlapSensorOffset, 0, -.0625], jointAxis='1 0 0')
        pyrosim.Send_Cube(name=str(botNum) + 'RightBottomSensor', pos=[0, 0, 0], size=[.25, .25, 0.125])

        # LEFTFLAP
        pyrosim.Send_Joint(name=str(botNum) + 'Torso_' + str(botNum) + 'LeftFlap', parent=str(botNum) + 'Torso', child=str(botNum) + 'LeftFlap',
                           type='revolute', position=[xCoord - 0.5, yCoord, zCoord], jointAxis='0 1 0')
        pyrosim.Send_Cube(name=str(botNum) + 'LeftFlap', pos=[-0.75 / 2, 0, 0], size=[.75, .5, 0.125])
        # Top Sensor
        pyrosim.Send_Joint(name=str(botNum) + 'LeftFlap_' + str(botNum) + 'LeftTopSensor', parent=str(botNum) + 'LeftFlap', child=str(botNum) + 'LeftTopSensor',
                           type='fixed', position=[-c.topFlapSensorOffset, 0, .0625], jointAxis='1 0 0')
        pyrosim.Send_Cube(name=str(botNum) + 'LeftTopSensor', pos=[0, 0, 0], size=[.25, .25, 0.125])
        # Bottom Sensor
        pyrosim.Send_Joint(name=str(botNum) + 'LeftFlap_' + str(botNum) + 'LeftBottomSensor', parent=str(botNum) + 'LeftFlap', child=str(botNum) + 'LeftBottomSensor',
                           type='fixed', position=[-c.bottomFlapSensorOffset, 0, -.0625], jointAxis='1 0 0')
        pyrosim.Send_Cube(name=str(botNum) + 'LeftBottomSensor', pos=[0, 0, 0], size=[.25, .25, 0.125])

        # UR LEG
        # Rotator Cuff
        pyrosim.Send_Joint(name=str(botNum) + 'Torso_' + str(botNum) + 'URRotate', parent=str(botNum) + 'Torso', child=str(botNum) + 'URRotate',
                           type='revolute', position=[xCoord - 0.5, yCoord - 0.5, zCoord], jointAxis='0 0 1')
        pyrosim.Send_Cube(name=str(botNum) + 'URRotate', pos=[0, 0, 0], size=[.2, .2, .2])
        # Top Leg
        pyrosim.Send_Joint(name=str(botNum) + 'URRotate_' + str(botNum) + 'URTopLeg', parent=str(botNum) + 'URRotate', child=str(botNum) + 'URTopLeg',
                           type='revolute', position=[0, 0, 0], jointAxis='0 1 0')
        pyrosim.Send_Cube(name=str(botNum) + 'URTopLeg', pos=[-.6, 0, 0], size=[1.2, .2, .2])
        # Bottom Leg
        pyrosim.Send_Joint(name=str(botNum) + 'URTopLeg_' + str(botNum) + 'URBottomLeg', parent=str(botNum) + 'URTopLeg', child=str(botNum) + 'URBottomLeg',
                           type='revolute', position=[-1.2, 0, 0], jointAxis='0 1 0')
        pyrosim.Send_Cube(name=str(botNum) + 'URBottomLeg', pos=[-0.5, 0, 0], size=[1, .2, .2])

        # UL LEG
        # Rotator Cuff
        pyrosim.Send_Joint(name=str(botNum) + 'Torso_' + str(botNum) + 'ULRotate', parent=str(botNum) + 'Torso', child=str(botNum) + 'ULRotate',
                           type='revolute', position=[xCoord - 0.5, yCoord + 0.5, zCoord], jointAxis='0 0 1')
        pyrosim.Send_Cube(name=str(botNum) + 'ULRotate', pos=[0, 0, 0], size=[.2, .2, .2])
        # Top Leg
        pyrosim.Send_Joint(name=str(botNum) + 'ULRotate_'+ str(botNum) + 'ULTopLeg', parent=str(botNum) + 'ULRotate', child=str(botNum) + 'ULTopLeg',
                           type='revolute', position=[0, 0, 0], jointAxis='0 1 0')
        pyrosim.Send_Cube(name=str(botNum) + 'ULTopLeg', pos=[-.6, 0, 0], size=[1.2, .2, .2])
        # Bottom Leg
        pyrosim.Send_Joint(name=str(botNum) + 'ULTopLeg_'+ str(botNum) + 'ULBottomLeg', parent=str(botNum) + 'ULTopLeg', child=str(botNum) + 'ULBottomLeg',
                           type='revolute', position=[-1.2, 0, 0], jointAxis='0 1 0')
        pyrosim.Send_Cube(name=str(botNum) + 'ULBottomLeg', pos=[-0.5, 0, 0], size=[1, .2, .2])

        # BR LEG
        # Rotator Cuff
        pyrosim.Send_Joint(name=str(botNum) + 'Torso_' + str(botNum) + 'BRRotate', parent=str(botNum) + 'Torso', child=str(botNum) + 'BRRotate',
                           type='revolute', position=[xCoord + 0.5, yCoord + 0.5, zCoord], jointAxis='0 0 1')
        pyrosim.Send_Cube(name=str(botNum) + 'BRRotate', pos=[0, 0, 0], size=[.2, .2, .2])
        # Top Leg
        pyrosim.Send_Joint(name=str(botNum) + 'BRRotate_' + str(botNum) + 'BRTopLeg', parent=str(botNum) + 'BRRotate', child=str(botNum) + 'BRTopLeg',
                           type='revolute', position=[0, 0, 0], jointAxis='0 1 0')
        pyrosim.Send_Cube(name=str(botNum) + 'BRTopLeg', pos=[.6, 0, 0], size=[1.2, .2, .2])
        # Bottom Leg
        pyrosim.Send_Joint(name=str(botNum) + 'BRTopLeg_'+ str(botNum) + 'BRBottomLeg', parent=str(botNum) + 'BRTopLeg', child=str(botNum) + 'BRBottomLeg',
                           type='revolute', position=[1.2, 0, 0], jointAxis='0 1 0')
        pyrosim.Send_Cube(name=str(botNum) + 'BRBottomLeg', pos=[0.5, 0, 0], size=[1, .2, .2])

        # BL LEG
        # Rotator Cuff
        pyrosim.Send_Joint(name=str(botNum) + 'Torso_' + str(botNum) + 'BLRotate', parent=str(botNum) + 'Torso', child=str(botNum) + 'BLRotate',
                           type='revolute', position=[xCoord + 0.5, yCoord - 0.5, zCoord], jointAxis='0 0 1')
        pyrosim.Send_Cube(name=str(botNum) + 'BLRotate', pos=[0, 0, 0], size=[.2, .2, .2])
        # Top Leg
        pyrosim.Send_Joint(name=str(botNum) + 'BLRotate_' + str(botNum) + 'BLTopLeg', parent=str(botNum) + 'BLRotate', child=str(botNum) + 'BLTopLeg',
                           type='revolute', position=[0, 0, 0], jointAxis='0 1 0')
        pyrosim.Send_Cube(name=str(botNum) + 'BLTopLeg', pos=[.6, 0, 0], size=[1.2, .2, .2])
        # Bottom Leg
        pyrosim.Send_Joint(name=str(botNum) + 'BLTopLeg_' + str(botNum) + 'BLBottomLeg', parent=str(botNum) + 'BLTopLeg', child=str(botNum) + 'BLBottomLeg',
                           type='revolute', position=[1.2, 0, 0], jointAxis='0 1 0')
        pyrosim.Send_Cube(name=str(botNum) + 'BLBottomLeg', pos=[0.5, 0, 0], size=[1, .2, .2])

        currentIndex = pyrosim.End()  # Close sdf file
        return currentIndex


def Generate_Brain(solutionID, bodyType, botNum, weights):
    pyrosim.Start_URDF('brain_' + str(solutionID) + str(bodyType) + str(botNum) + '.nndf', 0, botNum)

    # Sensors for Cubes
    # Torso Sensors
    pyrosim.Send_Sensor_Neuron(name=39*botNum + 0, linkName=str(botNum) + 'Torso')
    pyrosim.Send_Sensor_Neuron(name=39*botNum + 1, linkName=str(botNum) + 'TopSensor')
    pyrosim.Send_Sensor_Neuron(name=39*botNum + 2, linkName=str(botNum) + 'BottomSensor')

    # Flaps
    pyrosim.Send_Sensor_Neuron(name=39*botNum + 3, linkName=str(botNum) + 'FrontFlap')
    pyrosim.Send_Sensor_Neuron(name=39*botNum + 4, linkName=str(botNum) + 'FrontTopSensor')
    pyrosim.Send_Sensor_Neuron(name=39*botNum + 5, linkName=str(botNum) + 'FrontBottomSensor')

    pyrosim.Send_Sensor_Neuron(name=39*botNum + 6, linkName=str(botNum) + 'BackFlap')
    pyrosim.Send_Sensor_Neuron(name=39*botNum + 7, linkName=str(botNum) + 'BackTopSensor')
    pyrosim.Send_Sensor_Neuron(name=39*botNum + 8, linkName=str(botNum) + 'BackBottomSensor')

    pyrosim.Send_Sensor_Neuron(name=39*botNum + 9, linkName=str(botNum) + 'RightFlap')
    pyrosim.Send_Sensor_Neuron(name=39*botNum + 10, linkName=str(botNum) + 'RightTopSensor')
    pyrosim.Send_Sensor_Neuron(name=39*botNum + 11, linkName=str(botNum) + 'RightBottomSensor')

    pyrosim.Send_Sensor_Neuron(name=39*botNum + 12, linkName=str(botNum) + 'LeftFlap')
    pyrosim.Send_Sensor_Neuron(name=39*botNum + 13, linkName=str(botNum) + 'LeftTopSensor')
    pyrosim.Send_Sensor_Neuron(name=39*botNum + 14, linkName=str(botNum) + 'LeftBottomSensor')

    # Legs
    pyrosim.Send_Sensor_Neuron(name=39*botNum + 15, linkName=str(botNum) + 'URTopLeg')
    pyrosim.Send_Sensor_Neuron(name=39*botNum + 16, linkName=str(botNum) + 'URBottomLeg')

    pyrosim.Send_Sensor_Neuron(name=39*botNum + 17, linkName=str(botNum) + 'ULTopLeg')
    pyrosim.Send_Sensor_Neuron(name=39*botNum + 18, linkName=str(botNum) + 'ULBottomLeg')

    pyrosim.Send_Sensor_Neuron(name=39*botNum + 19, linkName=str(botNum) + 'BRTopLeg')
    pyrosim.Send_Sensor_Neuron(name=39*botNum + 20, linkName=str(botNum) + 'BRBottomLeg')

    pyrosim.Send_Sensor_Neuron(name=39*botNum + 21, linkName=str(botNum) + 'BLTopLeg')
    pyrosim.Send_Sensor_Neuron(name=39*botNum + 22, linkName=str(botNum) + 'BLBottomLeg')

    ### MOTORS ###

    ## Flaps ##
    pyrosim.Send_Motor_Neuron(name=39*botNum + 23, jointName=str(botNum) + 'Torso_' + str(botNum) + 'FrontFlap')
    pyrosim.Send_Motor_Neuron(name=39*botNum + 24, jointName=str(botNum) + 'Torso_' + str(botNum) + 'BackFlap')
    pyrosim.Send_Motor_Neuron(name=39*botNum + 25, jointName=str(botNum) + 'Torso_' + str(botNum) + 'RightFlap')
    pyrosim.Send_Motor_Neuron(name=39*botNum + 26, jointName=str(botNum) + 'Torso_' + str(botNum) + 'LeftFlap')

    ## Legs ##
    # Upper Right #
    pyrosim.Send_Motor_Neuron(name=39*botNum + 27, jointName=str(botNum) + 'Torso_' + str(botNum) + 'URRotate')
    pyrosim.Send_Motor_Neuron(name=39*botNum + 28, jointName=str(botNum) + 'URRotate_' + str(botNum) + 'URTopLeg')
    pyrosim.Send_Motor_Neuron(name=39*botNum + 29, jointName=str(botNum) + 'URTopLeg_' + str(botNum) + 'URBottomLeg')

    # Upper Left #
    pyrosim.Send_Motor_Neuron(name=39*botNum + 30, jointName=str(botNum) + 'Torso_' + str(botNum) + 'ULRotate')
    pyrosim.Send_Motor_Neuron(name=39*botNum + 31, jointName=str(botNum) + 'ULRotate_' + str(botNum) + 'ULTopLeg')
    pyrosim.Send_Motor_Neuron(name=39*botNum + 32, jointName=str(botNum) + 'ULTopLeg_' + str(botNum) + 'ULBottomLeg')

    # Back Right #
    pyrosim.Send_Motor_Neuron(name=39*botNum + 33, jointName=str(botNum) + 'Torso_' + str(botNum) + 'BRRotate')
    pyrosim.Send_Motor_Neuron(name=39*botNum + 34, jointName=str(botNum) + 'BRRotate_' + str(botNum) + 'BRTopLeg')
    pyrosim.Send_Motor_Neuron(name=39*botNum + 35, jointName=str(botNum) + 'BRTopLeg_' + str(botNum) + 'BRBottomLeg')

    # Back Left #
    pyrosim.Send_Motor_Neuron(name=39*botNum + 36, jointName=str(botNum) + 'Torso_' + str(botNum) + 'BLRotate')
    pyrosim.Send_Motor_Neuron(name=39*botNum + 37, jointName=str(botNum) + 'BLRotate_' + str(botNum) + 'BLTopLeg')
    pyrosim.Send_Motor_Neuron(name=39*botNum + 38, jointName=str(botNum) + 'BLTopLeg_' + str(botNum) + 'BLBottomLeg')

    # for sensor_name in range(39*botNum, 39*botNum + c.numSensorNeurons):
    #     for motor in range(botNum*39 + c.numSensorNeurons, botNum*39 + c.numSensorNeurons + c.numMotorNeurons):
    #         pyrosim.Send_Synapse(sourceNeuronName=sensor_name, targetNeuronName=motor, weight=2 * random.random() - 1)

    for currentRow in range(c.numSensorNeurons):
        for currentColumn in range(c.numMotorNeurons):
            pyrosim.Send_Synapse(sourceNeuronName=currentRow + (39*botNum),
                                 targetNeuronName=currentColumn + (39*botNum) + c.numSensorNeurons,
                                 weight= weights[currentRow][currentColumn])

    endingIndex = pyrosim.End()

def Generate_Rigidity(bodyType, jointName, numBots):
    if bodyType == 'A':
        for botNum in range(numBots):
            if jointName == str(botNum) + 'Torso_' + str(botNum) + 'FrontFlap':

                return -c.TORSO_FLAP_ANGLE

            elif jointName == str(botNum) + 'Torso_' + str(botNum) + 'BackFlap':

                return c.TORSO_FLAP_ANGLE

            elif jointName == str(botNum) + 'Torso_' + str(botNum) + 'RightFlap':

                return c.TORSO_FLAP_ANGLE

            elif jointName == str(botNum) + 'Torso_' + str(botNum) + 'LeftFlap':

                return -c.TORSO_FLAP_ANGLE

            elif jointName == str(botNum) + 'Torso_' + str(botNum) + 'URRotate':

                return c.ROTATOR_ANGLE

            elif jointName == str(botNum) + 'URRotate_' + str(botNum) + 'URTopLeg':

                return c.TOP_LEG_ANGLE

            elif jointName == str(botNum) + 'URTopLeg_' + str(botNum) + 'URBottomLeg':

                return -c.BOTTOM_LEG_ANGLE

            elif jointName == str(botNum) + 'Torso_' + str(botNum) + 'ULRotate':

                return -c.ROTATOR_ANGLE

            elif jointName == str(botNum) + 'ULRotate_' + str(botNum) + 'ULTopLeg':

                return c.TOP_LEG_ANGLE

            elif jointName == str(botNum) + 'ULTopLeg_' + str(botNum) + 'ULBottomLeg':

                return -c.BOTTOM_LEG_ANGLE

            elif jointName == str(botNum) + 'Torso_' + str(botNum) + 'BRRotate':

                return c.ROTATOR_ANGLE

            elif jointName == str(botNum) + 'BRRotate_' + str(botNum) + 'BRTopLeg':

                return -c.TOP_LEG_ANGLE

            elif jointName == str(botNum) + 'BRTopLeg_' + str(botNum) + 'BRBottomLeg':

                return c.BOTTOM_LEG_ANGLE

            elif jointName == str(botNum) + 'Torso_' + str(botNum) + 'BLRotate':

                return -c.ROTATOR_ANGLE

            elif jointName == str(botNum) + 'BLRotate_' + str(botNum) + 'BLTopLeg':

                return -c.TOP_LEG_ANGLE

            elif jointName == str(botNum) + 'BLTopLeg_' + str(botNum) + 'BLBottomLeg':

                return c.BOTTOM_LEG_ANGLE


def Generate_Oscillation(bodyType, jointName, numBots):
    if bodyType == 'A':
        if c.RANDOM == True:

            amplitude = np.random.random_sample() * 2 * np.pi - np.pi
            frequency = np.random.random_sample() * 2 * np.pi - np.pi
            offset = np.random.random_sample() * 2 * np.pi - np.pi

            x = np.linspace(start=0 - offset, stop=2 * np.pi - offset, num=c.FRAMES) * frequency

            motorValues = np.sin(x) * amplitude

            return motorValues

        for botNum in range(numBots):
            # TESTING 1 different bot
            if c.DIFFERENT_BEHAVIOR:
                if botNum == 1:
                    # Testing that the bots can move differently
                    if jointName in [str(botNum) + 'Torso_' + str(botNum) + 'FrontFlap',
                                     str(botNum) + 'Torso_' + str(botNum) + 'BackFlap',
                                     str(botNum) + 'Torso_' + str(botNum) + 'RightFlap',
                                     str(botNum) + 'Torso_' + str(botNum) + 'LeftFlap']:

                        amplitude = 0
                        frequency = 0
                        offset = 0

                        x = np.linspace(start=0 - offset, stop=2 * np.pi - offset, num=c.FRAMES) * frequency

                        if jointName in [str(botNum) + 'Torso_' + str(botNum) + 'FrontFlap',
                                         str(botNum) + 'Torso_' + str(botNum) + 'RightFlap']:
                            motorValues = np.sin(x) * amplitude - c.FLAP_TRANSLATION
                        else:
                            motorValues = np.sin(x) * amplitude + c.FLAP_TRANSLATION

                        return motorValues

                    elif jointName == str(botNum) + 'Torso_' + str(botNum) + 'URRotate':

                        amplitude = 0
                        frequency = 0
                        offset = 0

                        x = np.linspace(start=0 - offset, stop=2 * np.pi - offset, num=c.FRAMES) * frequency

                        motorValues = np.sin(x) * amplitude + c.ROTATOR_TRANSLATION

                        return motorValues

                    elif jointName == str(botNum) + 'URRotate_' + str(botNum) + 'URTopLeg':

                        amplitude = 0
                        frequency = 0
                        offset = 0

                        x = np.linspace(start=0 - offset, stop=2 * np.pi - offset, num=c.FRAMES) * frequency

                        motorValues = np.sin(x) * amplitude

                        return motorValues

                    elif jointName == str(botNum) + 'URTopLeg_' + str(botNum) + 'URBottomLeg':

                        amplitude = 0
                        frequency = 0
                        offset = 0

                        x = np.linspace(start=0 - offset, stop=2 * np.pi - offset, num=c.FRAMES) * frequency

                        motorValues = np.sin(x) * amplitude - c.LOWER_LEG_TRANSLATION

                        return motorValues

                    elif jointName == str(botNum) + 'Torso_' + str(botNum) + 'ULRotate':

                        amplitude = 0
                        frequency = 0
                        offset = 0 + 0

                        x = np.linspace(start=0 - offset, stop=2 * np.pi - offset, num=c.FRAMES) * frequency

                        motorValues = np.sin(x) * amplitude

                        return motorValues

                    elif jointName == str(botNum) + 'ULRotate_' + str(botNum) + 'ULTopLeg':

                        amplitude = 0
                        frequency = 0
                        offset = 0

                        x = np.linspace(start=0 - offset, stop=2 * np.pi - offset, num=c.FRAMES) * frequency

                        motorValues = np.sin(x) * amplitude

                        return motorValues

                    elif jointName == str(botNum) + 'ULTopLeg_' + str(botNum) + 'ULBottomLeg':

                        amplitude = 0
                        frequency = 0
                        offset = 0

                        x = np.linspace(start=0 - offset, stop=2 * np.pi - offset, num=c.FRAMES) * frequency

                        motorValues = np.sin(x) * amplitude - c.LOWER_LEG_TRANSLATION

                        return motorValues

                    elif jointName == str(botNum) + 'Torso_' + str(botNum) + 'BRRotate':

                        amplitude = 0
                        frequency = 0
                        offset = 0 + 0

                        x = np.linspace(start=0 - offset, stop=2 * np.pi - offset, num=c.FRAMES) * frequency

                        motorValues = np.sin(x) * amplitude

                        return motorValues

                    elif jointName == str(botNum) + 'BRRotate_' + str(botNum) + 'BRTopLeg':

                        amplitude = 0
                        frequency = 0
                        offset = 0

                        x = np.linspace(start=0 - offset, stop=2 * np.pi - offset, num=c.FRAMES) * frequency

                        motorValues = np.sin(x) * amplitude

                        return motorValues

                    elif jointName == str(botNum) + 'BRTopLeg_' + str(botNum) + 'BRBottomLeg':

                        amplitude = 0
                        frequency = 0
                        offset = 0

                        x = np.linspace(start=0 - offset, stop=2 * np.pi - offset, num=c.FRAMES) * frequency

                        motorValues = np.sin(x) * amplitude + c.LOWER_LEG_TRANSLATION

                        return motorValues

                    elif jointName == str(botNum) + 'Torso_' + str(botNum) + 'BLRotate':

                        amplitude = 0
                        frequency = 0
                        offset = 0

                        x = np.linspace(start=0 - offset, stop=2 * np.pi - offset, num=c.FRAMES) * frequency

                        motorValues = np.sin(x) * amplitude

                        return motorValues

                    elif jointName == str(botNum) + 'BLRotate_' + str(botNum) + 'BLTopLeg':

                        amplitude = 0
                        frequency = 0
                        offset = 0

                        x = np.linspace(start=0 - offset, stop=2 * np.pi - offset, num=c.FRAMES) * frequency

                        motorValues = np.sin(x) * amplitude

                        return motorValues

                    elif jointName == str(botNum) + 'BLTopLeg_' + str(botNum) + 'BLBottomLeg':

                        amplitude = 0
                        frequency = 0
                        offset = 0

                        x = np.linspace(start=0 - offset, stop=2 * np.pi - offset, num=c.FRAMES) * frequency

                        motorValues = np.sin(x) * amplitude + c.LOWER_LEG_TRANSLATION

                        return motorValues
                else:
                    if jointName in [str(botNum) + 'Torso_' + str(botNum) + 'FrontFlap',
                                     str(botNum) + 'Torso_' + str(botNum) + 'BackFlap',
                                     str(botNum) + 'Torso_' + str(botNum) + 'RightFlap',
                                     str(botNum) + 'Torso_' + str(botNum) + 'LeftFlap']:

                        amplitude = c.FLAP_AMPS
                        frequency = c.FLAP_FREQ
                        offset = c.FLAP_OFFSET

                        x = np.linspace(start=0 - offset, stop=2 * np.pi - offset, num=c.FRAMES) * frequency

                        if jointName in [str(botNum) + 'Torso_' + str(botNum) + 'FrontFlap',
                                         str(botNum) + 'Torso_' + str(botNum) + 'RightFlap']:
                            motorValues = np.sin(x) * amplitude - c.FLAP_TRANSLATION
                        else:
                            motorValues = np.sin(x) * amplitude + c.FLAP_TRANSLATION

                        return motorValues

                    elif jointName == str(botNum) + 'Torso_' + str(botNum) + 'URRotate':

                        amplitude = c.ROTATOR_AMPS
                        frequency = c.ROTATOR_FREQ
                        offset = c.ROTATOR_OFFSET

                        x = np.linspace(start=0 - offset, stop=2 * np.pi - offset, num=c.FRAMES) * frequency

                        motorValues = np.sin(x) * amplitude + c.ROTATOR_TRANSLATION

                        return motorValues

                    elif jointName == str(botNum) + 'URRotate_' + str(botNum) + 'URTopLeg':

                        amplitude = c.UPPER_LEG_AMPS
                        frequency = c.UPPER_LEG_FREQ
                        offset = c.UPPER_LEG_OFFSET

                        x = np.linspace(start=0 - offset, stop=2 * np.pi - offset, num=c.FRAMES) * frequency

                        motorValues = np.sin(x) * amplitude

                        return motorValues

                    elif jointName == str(botNum) + 'URTopLeg_' + str(botNum) + 'URBottomLeg':

                        amplitude = c.LOWER_LEG_AMPS
                        frequency = c.LOWER_LEG_FREQ
                        offset = c.LOWER_LEG_OFFSET

                        x = np.linspace(start=0 - offset, stop=2 * np.pi - offset, num=c.FRAMES) * frequency

                        motorValues = np.sin(x) * amplitude - c.LOWER_LEG_TRANSLATION

                        return motorValues

                    elif jointName == str(botNum) + 'Torso_' + str(botNum) + 'ULRotate':

                        amplitude = c.ROTATOR_AMPS
                        frequency = c.ROTATOR_FREQ
                        offset = c.ROTATOR_OFFSET + c.ROTATOR_TRANSLATION

                        x = np.linspace(start=0 - offset, stop=2 * np.pi - offset, num=c.FRAMES) * frequency

                        motorValues = np.sin(x) * amplitude

                        return motorValues

                    elif jointName == str(botNum) + 'ULRotate_' + str(botNum) + 'ULTopLeg':

                        amplitude = c.UPPER_LEG_AMPS
                        frequency = c.UPPER_LEG_FREQ
                        offset = c.UPPER_LEG_OFFSET

                        x = np.linspace(start=0 - offset, stop=2 * np.pi - offset, num=c.FRAMES) * frequency

                        motorValues = np.sin(x) * amplitude

                        return motorValues

                    elif jointName == str(botNum) + 'ULTopLeg_' + str(botNum) + 'ULBottomLeg':

                        amplitude = c.LOWER_LEG_AMPS
                        frequency = c.LOWER_LEG_FREQ
                        offset = c.LOWER_LEG_OFFSET

                        x = np.linspace(start=0 - offset, stop=2 * np.pi - offset, num=c.FRAMES) * frequency

                        motorValues = np.sin(x) * amplitude - c.LOWER_LEG_TRANSLATION

                        return motorValues

                    elif jointName == str(botNum) + 'Torso_' + str(botNum) + 'BRRotate':

                        amplitude = c.ROTATOR_AMPS
                        frequency = c.ROTATOR_FREQ
                        offset = c.ROTATOR_OFFSET + c.ROTATOR_TRANSLATION

                        x = np.linspace(start=0 - offset, stop=2 * np.pi - offset, num=c.FRAMES) * frequency

                        motorValues = np.sin(x) * amplitude

                        return motorValues

                    elif jointName == str(botNum) + 'BRRotate_' + str(botNum) + 'BRTopLeg':

                        amplitude = c.UPPER_LEG_AMPS
                        frequency = c.UPPER_LEG_FREQ
                        offset = c.UPPER_LEG_OFFSET

                        x = np.linspace(start=0 - offset, stop=2 * np.pi - offset, num=c.FRAMES) * frequency

                        motorValues = np.sin(x) * amplitude

                        return motorValues

                    elif jointName == str(botNum) + 'BRTopLeg_' + str(botNum) + 'BRBottomLeg':

                        amplitude = c.LOWER_LEG_AMPS
                        frequency = c.LOWER_LEG_FREQ
                        offset = c.LOWER_LEG_OFFSET

                        x = np.linspace(start=0 - offset, stop=2 * np.pi - offset, num=c.FRAMES) * frequency

                        motorValues = np.sin(x) * amplitude + c.LOWER_LEG_TRANSLATION

                        return motorValues

                    elif jointName == str(botNum) + 'Torso_' + str(botNum) + 'BLRotate':

                        amplitude = c.ROTATOR_AMPS
                        frequency = c.ROTATOR_FREQ
                        offset = c.ROTATOR_OFFSET - c.ROTATOR_TRANSLATION

                        x = np.linspace(start=0 - offset, stop=2 * np.pi - offset, num=c.FRAMES) * frequency

                        motorValues = np.sin(x) * amplitude

                        return motorValues

                    elif jointName == str(botNum) + 'BLRotate_' + str(botNum) + 'BLTopLeg':

                        amplitude = c.UPPER_LEG_AMPS
                        frequency = c.UPPER_LEG_FREQ
                        offset = c.UPPER_LEG_OFFSET

                        x = np.linspace(start=0 - offset, stop=2 * np.pi - offset, num=c.FRAMES) * frequency

                        motorValues = np.sin(x) * amplitude

                        return motorValues

                    elif jointName == str(botNum) + 'BLTopLeg_' + str(botNum) + 'BLBottomLeg':

                        amplitude = c.LOWER_LEG_AMPS
                        frequency = c.LOWER_LEG_FREQ
                        offset = c.LOWER_LEG_OFFSET

                        x = np.linspace(start=0 - offset, stop=2 * np.pi - offset, num=c.FRAMES) * frequency

                        motorValues = np.sin(x) * amplitude + c.LOWER_LEG_TRANSLATION

                        return motorValues
            # Regular
            else:
                if jointName in [str(botNum) + 'Torso_' + str(botNum) + 'FrontFlap',
                                 str(botNum) + 'Torso_' + str(botNum) + 'BackFlap',
                                 str(botNum) + 'Torso_' + str(botNum) + 'RightFlap',
                                 str(botNum) + 'Torso_' + str(botNum) + 'LeftFlap']:

                    amplitude = c.FLAP_AMPS
                    frequency = c.FLAP_FREQ
                    offset = c.FLAP_OFFSET

                    x = np.linspace(start=0 - offset, stop=2 * np.pi - offset, num=c.FRAMES) * frequency

                    if jointName in [str(botNum) + 'Torso_' + str(botNum) + 'FrontFlap',
                                     str(botNum) + 'Torso_' + str(botNum) + 'RightFlap']:
                        motorValues = np.sin(x) * amplitude - c.FLAP_TRANSLATION
                    else:
                        motorValues = np.sin(x) * amplitude + c.FLAP_TRANSLATION

                    return motorValues

                elif jointName == str(botNum) + 'Torso_' + str(botNum) + 'URRotate':

                    amplitude = c.ROTATOR_AMPS
                    frequency = c.ROTATOR_FREQ
                    offset = c.ROTATOR_OFFSET

                    x = np.linspace(start=0 - offset, stop=2 * np.pi - offset, num=c.FRAMES) * frequency

                    motorValues = np.sin(x) * amplitude + c.ROTATOR_TRANSLATION

                    return motorValues

                elif jointName == str(botNum) + 'URRotate_' + str(botNum) + 'URTopLeg':

                    amplitude = c.UPPER_LEG_AMPS
                    frequency = c.UPPER_LEG_FREQ
                    offset = c.UPPER_LEG_OFFSET

                    x = np.linspace(start=0 - offset, stop=2 * np.pi - offset, num=c.FRAMES) * frequency

                    motorValues = np.sin(x) * amplitude

                    return motorValues

                elif jointName == str(botNum) + 'URTopLeg_' + str(botNum) + 'URBottomLeg':

                    amplitude = c.LOWER_LEG_AMPS
                    frequency = c.LOWER_LEG_FREQ
                    offset = c.LOWER_LEG_OFFSET

                    x = np.linspace(start=0 - offset, stop=2 * np.pi - offset, num=c.FRAMES) * frequency

                    motorValues = np.sin(x) * amplitude - c.LOWER_LEG_TRANSLATION

                    return motorValues

                elif jointName == str(botNum) + 'Torso_' + str(botNum) + 'ULRotate':

                    amplitude = c.ROTATOR_AMPS
                    frequency = c.ROTATOR_FREQ
                    offset = c.ROTATOR_OFFSET + c.ROTATOR_TRANSLATION

                    x = np.linspace(start=0 - offset, stop=2 * np.pi - offset, num=c.FRAMES) * frequency

                    motorValues = np.sin(x) * amplitude

                    return motorValues

                elif jointName == str(botNum) + 'ULRotate_' + str(botNum) + 'ULTopLeg':

                    amplitude = c.UPPER_LEG_AMPS
                    frequency = c.UPPER_LEG_FREQ
                    offset = c.UPPER_LEG_OFFSET

                    x = np.linspace(start=0 - offset, stop=2 * np.pi - offset, num=c.FRAMES) * frequency

                    motorValues = np.sin(x) * amplitude

                    return motorValues

                elif jointName == str(botNum) + 'ULTopLeg_' + str(botNum) + 'ULBottomLeg':

                    amplitude = c.LOWER_LEG_AMPS
                    frequency = c.LOWER_LEG_FREQ
                    offset = c.LOWER_LEG_OFFSET

                    x = np.linspace(start=0 - offset, stop=2 * np.pi - offset, num=c.FRAMES) * frequency

                    motorValues = np.sin(x) * amplitude - c.LOWER_LEG_TRANSLATION

                    return motorValues

                elif jointName == str(botNum) + 'Torso_' + str(botNum) + 'BRRotate':

                    amplitude = c.ROTATOR_AMPS
                    frequency = c.ROTATOR_FREQ
                    offset = c.ROTATOR_OFFSET + c.ROTATOR_TRANSLATION

                    x = np.linspace(start=0 - offset, stop=2 * np.pi - offset, num=c.FRAMES) * frequency

                    motorValues = np.sin(x) * amplitude

                    return motorValues

                elif jointName == str(botNum) + 'BRRotate_' + str(botNum) + 'BRTopLeg':

                    amplitude = c.UPPER_LEG_AMPS
                    frequency = c.UPPER_LEG_FREQ
                    offset = c.UPPER_LEG_OFFSET

                    x = np.linspace(start=0 - offset, stop=2 * np.pi - offset, num=c.FRAMES) * frequency

                    motorValues = np.sin(x) * amplitude

                    return motorValues

                elif jointName == str(botNum) + 'BRTopLeg_' + str(botNum) + 'BRBottomLeg':

                    amplitude = c.LOWER_LEG_AMPS
                    frequency = c.LOWER_LEG_FREQ
                    offset = c.LOWER_LEG_OFFSET

                    x = np.linspace(start=0 - offset, stop=2 * np.pi - offset, num=c.FRAMES) * frequency

                    motorValues = np.sin(x) * amplitude + c.LOWER_LEG_TRANSLATION

                    return motorValues

                elif jointName == str(botNum) + 'Torso_' + str(botNum) + 'BLRotate':

                    amplitude = c.ROTATOR_AMPS
                    frequency = c.ROTATOR_FREQ
                    offset = c.ROTATOR_OFFSET - c.ROTATOR_TRANSLATION

                    x = np.linspace(start=0 - offset, stop=2 * np.pi - offset, num=c.FRAMES) * frequency

                    motorValues = np.sin(x) * amplitude

                    return motorValues

                elif jointName == str(botNum) + 'BLRotate_' + str(botNum) + 'BLTopLeg':

                    amplitude = c.UPPER_LEG_AMPS
                    frequency = c.UPPER_LEG_FREQ
                    offset = c.UPPER_LEG_OFFSET

                    x = np.linspace(start=0 - offset, stop=2 * np.pi - offset, num=c.FRAMES) * frequency

                    motorValues = np.sin(x) * amplitude

                    return motorValues

                elif jointName == str(botNum) + 'BLTopLeg_' + str(botNum) + 'BLBottomLeg':

                    amplitude = c.LOWER_LEG_AMPS
                    frequency = c.LOWER_LEG_FREQ
                    offset = c.LOWER_LEG_OFFSET

                    x = np.linspace(start=0 - offset, stop=2 * np.pi - offset, num=c.FRAMES) * frequency

                    motorValues = np.sin(x) * amplitude + c.LOWER_LEG_TRANSLATION

                    return motorValues