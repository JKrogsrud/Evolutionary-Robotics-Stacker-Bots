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

        # # FRONTFLAP
        # pyrosim.Send_Joint(name=str(botNum) + 'Torso_' + str(botNum) + 'FrontFlap', parent=str(botNum) + 'Torso', child=str(botNum) + 'FrontFlap',
        #                    type='revolute', position=[xCoord, yCoord + 0.5, zCoord], jointAxis='1 0 0')
        # pyrosim.Send_Cube(name=str(botNum) + 'FrontFlap', pos=[0, 0.75 / 2, 0], size=[.5, .75, 0.125])
        # # Top Sensor
        # pyrosim.Send_Joint(name=str(botNum) + 'FrontFlap_' + str(botNum) + 'FrontTopSensor', parent=str(botNum) + 'FrontFlap', child=str(botNum) + 'FrontTopSensor',
        #                    type='fixed', position=[0, c.topFlapSensorOffset, .0625], jointAxis='1 0 0')
        # pyrosim.Send_Cube(name=str(botNum) + 'FrontTopSensor', pos=[0, 0, 0], size=[.25, .25, 0.125])
        # # Bottom Sensor
        # pyrosim.Send_Joint(name=str(botNum) + 'FrontFlap_' + str(botNum) + 'FrontBottomSensor', parent=str(botNum) + 'FrontFlap', child=str(botNum) + 'FrontBottomSensor',
        #                    type='fixed', position=[0, c.bottomFlapSensorOffset, -.0625], jointAxis='1 0 0')
        # pyrosim.Send_Cube(name=str(botNum) + 'FrontBottomSensor', pos=[0, 0, 0], size=[.25, .25, 0.125])

        # # BACKFLAP
        # pyrosim.Send_Joint(name=str(botNum) + 'Torso_'+ str(botNum) + 'BackFlap', parent=str(botNum) + 'Torso', child=str(botNum) + 'BackFlap',
        #                    type='revolute', position=[xCoord, yCoord - 0.5, zCoord], jointAxis='1 0 0')
        # pyrosim.Send_Cube(name=str(botNum) + 'BackFlap', pos=[0, -0.75 / 2, 0], size=[.5, .75, 0.125])
        # # Top Sensor
        # pyrosim.Send_Joint(name=str(botNum) + 'BackFlap_' + str(botNum) + 'BackTopSensor', parent=str(botNum) + 'BackFlap', child=str(botNum) + 'BackTopSensor',
        #                    type='fixed', position=[0, -c.topFlapSensorOffset, .0625], jointAxis='1 0 0')
        # pyrosim.Send_Cube(name=str(botNum) + 'BackTopSensor', pos=[0, 0, 0], size=[.25, .25, 0.125])
        # # Bottom Sensor
        # pyrosim.Send_Joint(name=str(botNum) + 'BackFlap_' + str(botNum) + 'BackBottomSensor', parent=str(botNum) + 'BackFlap', child=str(botNum) + 'BackBottomSensor',
        #                    type='fixed', position=[0, -c.bottomFlapSensorOffset, -.0625], jointAxis='1 0 0')
        # pyrosim.Send_Cube(name=str(botNum) + 'BackBottomSensor', pos=[0, 0, 0], size=[.25, .25, 0.125])

        # # RIGHTFLAP
        # pyrosim.Send_Joint(name=str(botNum) + 'Torso_' + str(botNum) + 'RightFlap', parent=str(botNum) + 'Torso', child=str(botNum) + 'RightFlap',
        #                    type='revolute', position=[xCoord + 0.5, yCoord, zCoord], jointAxis='0 1 0')
        # pyrosim.Send_Cube(name=str(botNum) + 'RightFlap', pos=[0.75 / 2, 0, 0], size=[.75, .5, 0.125])
        # # Top Sensor
        # pyrosim.Send_Joint(name=str(botNum) + 'RightFlap_'+ str(botNum) + 'RightTopSensor', parent=str(botNum) + 'RightFlap', child=str(botNum) + 'RightTopSensor',
        #                    type='fixed', position=[c.topFlapSensorOffset, 0, .0625], jointAxis='1 0 0')
        # pyrosim.Send_Cube(name=str(botNum) + 'RightTopSensor', pos=[0, 0, 0], size=[.25, .25, 0.125])
        # # Bottom Sensor
        # pyrosim.Send_Joint(name=str(botNum) + 'RightFlap_'+ str(botNum) + 'RightBottomSensor', parent=str(botNum) + 'RightFlap', child=str(botNum) + 'RightBottomSensor',
        #                    type='fixed', position=[c.bottomFlapSensorOffset, 0, -.0625], jointAxis='1 0 0')
        # pyrosim.Send_Cube(name=str(botNum) + 'RightBottomSensor', pos=[0, 0, 0], size=[.25, .25, 0.125])

        # # LEFTFLAP
        # pyrosim.Send_Joint(name=str(botNum) + 'Torso_' + str(botNum) + 'LeftFlap', parent=str(botNum) + 'Torso', child=str(botNum) + 'LeftFlap',
        #                    type='revolute', position=[xCoord - 0.5, yCoord, zCoord], jointAxis='0 1 0')
        # pyrosim.Send_Cube(name=str(botNum) + 'LeftFlap', pos=[-0.75 / 2, 0, 0], size=[.75, .5, 0.125])
        # # Top Sensor
        # pyrosim.Send_Joint(name=str(botNum) + 'LeftFlap_' + str(botNum) + 'LeftTopSensor', parent=str(botNum) + 'LeftFlap', child=str(botNum) + 'LeftTopSensor',
        #                    type='fixed', position=[-c.topFlapSensorOffset, 0, .0625], jointAxis='1 0 0')
        # pyrosim.Send_Cube(name=str(botNum) + 'LeftTopSensor', pos=[0, 0, 0], size=[.25, .25, 0.125])
        # # Bottom Sensor
        # pyrosim.Send_Joint(name=str(botNum) + 'LeftFlap_' + str(botNum) + 'LeftBottomSensor', parent=str(botNum) + 'LeftFlap', child=str(botNum) + 'LeftBottomSensor',
        #                    type='fixed', position=[-c.bottomFlapSensorOffset, 0, -.0625], jointAxis='1 0 0')
        # pyrosim.Send_Cube(name=str(botNum) + 'LeftBottomSensor', pos=[0, 0, 0], size=[.25, .25, 0.125])

        # UR LEG
        # Rotator Cuff
        pyrosim.Send_Joint(name=str(botNum) + 'Torso_' + str(botNum) + 'URRotate', parent=str(botNum) + 'Torso', child=str(botNum) + 'URRotate',
                           type='revolute', position=[xCoord - 0.5, yCoord - 0.5, zCoord], jointAxis='0 0 1')
        pyrosim.Send_Cube(name=str(botNum) + 'URRotate', pos=[0, 0, 0], size=[.2, .2, .2])
        # Top Leg
        pyrosim.Send_Joint(name=str(botNum) + 'URRotate_' + str(botNum) + 'URTopLeg', parent=str(botNum) + 'URRotate', child=str(botNum) + 'URTopLeg',
                           type='revolute', position=[0, 0, 0], jointAxis='0 1 0')
        pyrosim.Send_Cube(name=str(botNum) + 'URTopLeg', pos=[-.6, 0, 0], size=[1.2, .2, .2], color=c.UR)
        # Bottom Leg
        pyrosim.Send_Joint(name=str(botNum) + 'URTopLeg_' + str(botNum) + 'URBottomLeg', parent=str(botNum) + 'URTopLeg', child=str(botNum) + 'URBottomLeg',
                           type='revolute', position=[-1.2, 0, 0], jointAxis='0 1 0')
        pyrosim.Send_Cube(name=str(botNum) + 'URBottomLeg', pos=[-0.5, 0, 0], size=[1, .2, .2], color=c.UR)

        # UL LEG
        # Rotator Cuff
        pyrosim.Send_Joint(name=str(botNum) + 'Torso_' + str(botNum) + 'ULRotate', parent=str(botNum) + 'Torso', child=str(botNum) + 'ULRotate',
                           type='revolute', position=[xCoord - 0.5, yCoord + 0.5, zCoord], jointAxis='0 0 1')
        pyrosim.Send_Cube(name=str(botNum) + 'ULRotate', pos=[0, 0, 0], size=[.2, .2, .2])
        # Top Leg
        pyrosim.Send_Joint(name=str(botNum) + 'ULRotate_'+ str(botNum) + 'ULTopLeg', parent=str(botNum) + 'ULRotate', child=str(botNum) + 'ULTopLeg',
                           type='revolute', position=[0, 0, 0], jointAxis='0 1 0')
        pyrosim.Send_Cube(name=str(botNum) + 'ULTopLeg', pos=[-.6, 0, 0], size=[1.2, .2, .2], color=c.UL)
        # Bottom Leg
        pyrosim.Send_Joint(name=str(botNum) + 'ULTopLeg_'+ str(botNum) + 'ULBottomLeg', parent=str(botNum) + 'ULTopLeg', child=str(botNum) + 'ULBottomLeg',
                           type='revolute', position=[-1.2, 0, 0], jointAxis='0 1 0')
        pyrosim.Send_Cube(name=str(botNum) + 'ULBottomLeg', pos=[-0.5, 0, 0], size=[1, .2, .2], color=c.UL)

        # BR LEG
        # Rotator Cuff
        pyrosim.Send_Joint(name=str(botNum) + 'Torso_' + str(botNum) + 'BRRotate', parent=str(botNum) + 'Torso', child=str(botNum) + 'BRRotate',
                           type='revolute', position=[xCoord + 0.5, yCoord + 0.5, zCoord], jointAxis='0 0 1')
        pyrosim.Send_Cube(name=str(botNum) + 'BRRotate', pos=[0, 0, 0], size=[.2, .2, .2])
        # Top Leg
        pyrosim.Send_Joint(name=str(botNum) + 'BRRotate_' + str(botNum) + 'BRTopLeg', parent=str(botNum) + 'BRRotate', child=str(botNum) + 'BRTopLeg',
                           type='revolute', position=[0, 0, 0], jointAxis='0 1 0')
        pyrosim.Send_Cube(name=str(botNum) + 'BRTopLeg', pos=[.6, 0, 0], size=[1.2, .2, .2], color=c.BR)
        # Bottom Leg
        pyrosim.Send_Joint(name=str(botNum) + 'BRTopLeg_' + str(botNum) + 'BRBottomLeg', parent=str(botNum) + 'BRTopLeg', child=str(botNum) + 'BRBottomLeg',
                           type='revolute', position=[1.2, 0, 0], jointAxis='0 1 0')
        pyrosim.Send_Cube(name=str(botNum) + 'BRBottomLeg', pos=[0.5, 0, 0], size=[1, .2, .2], color=c.BR)

        # BL LEG
        # Rotator Cuff
        pyrosim.Send_Joint(name=str(botNum) + 'Torso_' + str(botNum) + 'BLRotate', parent=str(botNum) + 'Torso', child=str(botNum) + 'BLRotate',
                           type='revolute', position=[xCoord + 0.5, yCoord - 0.5, zCoord], jointAxis='0 0 1')
        pyrosim.Send_Cube(name=str(botNum) + 'BLRotate', pos=[0, 0, 0], size=[.2, .2, .2])
        # Top Leg
        pyrosim.Send_Joint(name=str(botNum) + 'BLRotate_' + str(botNum) + 'BLTopLeg', parent=str(botNum) + 'BLRotate', child=str(botNum) + 'BLTopLeg',
                           type='revolute', position=[0, 0, 0], jointAxis='0 1 0')
        pyrosim.Send_Cube(name=str(botNum) + 'BLTopLeg', pos=[.6, 0, 0], size=[1.2, .2, .2], color=c.BL)
        # Bottom Leg
        pyrosim.Send_Joint(name=str(botNum) + 'BLTopLeg_' + str(botNum) + 'BLBottomLeg', parent=str(botNum) + 'BLTopLeg', child=str(botNum) + 'BLBottomLeg',
                           type='revolute', position=[1.2, 0, 0], jointAxis='0 1 0')
        pyrosim.Send_Cube(name=str(botNum) + 'BLBottomLeg', pos=[0.5, 0, 0], size=[1, .2, .2], color=c.BL)

        currentIndex = pyrosim.End()  # Close sdf file
        return currentIndex


def Generate_Brain(solutionID, bodyType, botNum, weight):
    pyrosim.Start_NeuralNetwork('brain_' + str(solutionID) + str(bodyType) + str(botNum) + '.nndf')

    SensorHiddenWeight = weight[0]
    HiddenMotorWeight = weight[1]

    if c.BRAIN_TYPE == 'neural_network_recurrant':
        HiddenHiddenWeight = weight[2]

    cubes = c.cube_sensors

    neuronIndex = 0

    neuronDict = {}
    neuronDict['Sensor'] = {}
    neuronDict['Hidden'] = {}
    neuronDict['Motor'] = {}

    ### Sensors ###
    neuronDict['Sensor']['startIndex'] = c.totalNeurons * botNum + neuronIndex
    for cube in cubes:
        pyrosim.Send_Sensor_Neuron(name=c.totalNeurons * botNum + neuronIndex, linkName=str(botNum) + str(cube))
        neuronIndex += 1
    neuronDict['Sensor']['endIndex'] = c.totalNeurons * botNum + neuronIndex

    ### Hidden ###
    neuronDict['Hidden']['startIndex'] = c.totalNeurons * botNum + neuronIndex
    for i in range(c.numHiddenNeurons):
        pyrosim.Send_Hidden_Neuron(name=c.totalNeurons*botNum + neuronIndex)
        neuronIndex += 1
    neuronDict['Hidden']['endIndex'] = c.totalNeurons * botNum + neuronIndex

    ### MOTORS ###
    motors = c.motors

    neuronDict['Motor']['startIndex'] = c.totalNeurons * botNum + neuronIndex
    for motor in motors:
        pyrosim.Send_Motor_Neuron(name=c.totalNeurons * botNum + neuronIndex,
                                  jointName=str(botNum) + str(motor[0]) + '_' + str(botNum) + str(motor[1]))
        neuronIndex += 1
    neuronDict['Motor']['endIndex'] = c.totalNeurons * botNum + neuronIndex

    ### Connect Sensors to hidden neurons ###
    ### Assume the appropriate array of synapse values have been passed in

    for currentRow in range(c.numSensorNeurons):
        for currentColumn in range(c.numHiddenNeurons):
            sourceNeuron = neuronDict['Sensor']['startIndex'] + currentRow
            targetNeuron = neuronDict['Hidden']['startIndex'] + currentColumn
            pyrosim.Send_Synapse(sourceNeuronName=sourceNeuron,
                                 targetNeuronName=targetNeuron,
                                 weight=SensorHiddenWeight[currentRow][currentColumn])

    for currentRow in range(c.numHiddenNeurons):
        for currentColumn in range(c.numMotorNeurons):
            sourceNeuron = neuronDict['Hidden']['startIndex'] + currentRow
            targetNeuron = neuronDict['Motor']['startIndex'] + currentColumn
            pyrosim.Send_Synapse(sourceNeuronName=sourceNeuron,
                                 targetNeuronName=targetNeuron,
                                 weight=HiddenMotorWeight[currentRow][currentColumn])

    # Attach Recurrant connections if needed
    if c.BRAIN_TYPE == 'neural_network_recurrant':
        for currentColumn in range(c.numHiddenNeurons):
            hiddenNeuron = neuronDict['Hidden']['startIndex'] + currentColumn
            pyrosim.Send_Synapse(sourceNeuronName=hiddenNeuron,
                                 targetNeuronName=hiddenNeuron,
                                 weight=HiddenHiddenWeight[0][currentColumn])

    endingIndex = pyrosim.End()

def Generate_Hive_Mind(solutionID, bodyType, weights):
    pyrosim.Start_NeuralNetwork('brain_' + str(solutionID) + str(bodyType) + '.nndf')

    cubes = c.cube_sensors

    if c.BRAIN_TYPE in {'hive_mind', 'hive_mind_recurrant'}:

        neuronIndex = 0

        neuronDict = {}
        neuronDict['Sensor'] = {}
        neuronDict['Hidden'] = {}
        neuronDict['Motor'] = {}

        # Attach Sensors to cubes
        neuronDict['Sensor']['startIndex'] = neuronIndex
        for botNum in range(c.numBots):
            for cube in cubes:
                pyrosim.Send_Sensor_Neuron(name=neuronIndex, linkName=str(botNum) + str(cube))
                neuronIndex += 1
        neuronDict['Sensor']['endIndex'] = neuronIndex

        # Create a Hidden Layer
        neuronDict['Hidden']['startIndex'] = neuronIndex
        for i in range(c.numHiddenNeurons):
            pyrosim.Send_Hidden_Neuron(name=neuronIndex)
            neuronIndex += 1
        neuronDict['Hidden']['endIndex'] = neuronIndex

        # Attach motors
        motors = c.motors

        neuronDict['Motor']['startIndex'] = neuronIndex
        for botNum in range(c.numBots):
            for motor in motors:
                pyrosim.Send_Motor_Neuron(name=neuronIndex,
                                          jointName=str(botNum) + str(motor[0]) + '_' + str(botNum) + str(motor[1]))
                neuronIndex += 1
        neuronDict['Motor']['endIndex'] = neuronIndex

        # Attaching Synapses
        # We need a c.numSensorNeurons * c.numBots by c.numHiddenNeurons array

        # Sensors to Hidden
        for currentRow in range(c.numSensorNeurons * c.numBots):
            for currentColumn in range(c.numHiddenNeurons):
                sourceNeuron = neuronDict['Sensor']['startIndex'] + currentRow
                targetNeuron = neuronDict['Hidden']['startIndex'] + currentColumn
                pyrosim.Send_Synapse(sourceNeuronName=sourceNeuron,
                                     targetNeuronName=targetNeuron,
                                     weight=weights[0][currentRow][currentColumn])
        # Hidden to Motors
        for currentRow in range(c.numHiddenNeurons):
            for currentColumn in range(c.numBots * c.numMotorNeurons):
                sourceNeuron = neuronDict['Hidden']['startIndex'] + currentRow
                targetNeuron = neuronDict['Motor']['startIndex'] + currentColumn
                pyrosim.Send_Synapse(sourceNeuronName=sourceNeuron,
                                     targetNeuronName=targetNeuron,
                                     weight=weights[1][currentRow][currentColumn])

        # Connect recurrant connections
        if c.BRAIN_TYPE == 'hive_mind_recurrant':
            for currentColumn in range(c.numHiddenNeurons):
                neuron = neuronDict['Hidden']['startIndex'] + currentColumn
                pyrosim.Send_Synapse(sourceNeuronName=neuron,
                                     targetNeuronName=neuron,
                                     weight=weights[2][0][currentColumn])

    if c.BRAIN_TYPE == 'hive_mind_recurrant_hybrid_A':

        neuronIndex = 0

        neuronDict = {}
        neuronDict['Sensor'] = {}
        neuronDict['HiddenHive'] = {}
        neuronDict['HiddenLocal'] = {}
        neuronDict['Motor'] = {}

        # Attach Sensors to cubes
        neuronDict['Sensor']['startIndex'] = neuronIndex
        for botNum in range(c.numBots):
            for cube in cubes:
                pyrosim.Send_Sensor_Neuron(name=neuronIndex, linkName=str(botNum) + str(cube))
                neuronIndex += 1
        neuronDict['Sensor']['endIndex'] = neuronIndex

        # Create a Hidden Hive Layer
        neuronDict['HiddenHive']['startIndex'] = neuronIndex
        for i in range(int(c.numHiddenNeurons / 2)):
            pyrosim.Send_Hidden_Neuron(name=neuronIndex)
            neuronIndex += 1
        neuronDict['HiddenHive']['endIndex'] = neuronIndex

        # Create a Hidden Local Layer
        neuronDict['HiddenLocal']['startIndex'] = neuronIndex
        for i in range(int(c.numHiddenNeurons / 2)):
            pyrosim.Send_Hidden_Neuron(name=neuronIndex)
            neuronIndex += 1
        neuronDict['HiddenLocal']['endIndex'] = neuronIndex

        # Attach Motors

        motors = c.motors

        neuronDict['Motor']['startIndex'] = neuronIndex
        for botNum in range(c.numBots):
            for motor in motors:
                pyrosim.Send_Motor_Neuron(name=neuronIndex,
                                          jointName=str(botNum) + str(motor[0]) + '_' + str(botNum) + str(motor[1]))
                neuronIndex += 1
        neuronDict['Motor']['endIndex'] = neuronIndex

        ## Attaching Synapses ##
        [sensorHiddenHive, sensorHiddenLocal, hiddenHiveMotor, hiddenLocalMotor, recurrantHive, recurrantLocal] = weights

        # Sensors to HiddenHive
        for currentRow in range(c.numSensorNeurons * c.numBots):
            for currentColumn in range(int(c.numHiddenNeurons / 2)):
                sourceNeuron = neuronDict['Sensor']['startIndex'] + currentRow
                targetNeuron = neuronDict['HiddenHive']['startIndex'] + currentColumn
                pyrosim.Send_Synapse(sourceNeuronName=sourceNeuron,
                                     targetNeuronName=targetNeuron,
                                     weight=sensorHiddenHive[currentRow][currentColumn])

        # Sensors to HiddenLocal
        for currentRow in range(c.numSensorNeurons * c.numBots):
            for currentColumn in range(int(c.numHiddenNeurons / 2)):
                sourceNeuron = neuronDict['Sensor']['startIndex'] + currentRow
                targetNeuron = neuronDict['HiddenLocal']['startIndex'] + currentColumn
                pyrosim.Send_Synapse(sourceNeuronName=sourceNeuron,
                                     targetNeuronName=targetNeuron,
                                     weight=sensorHiddenLocal[currentRow][currentColumn])

        # HiddenHive to Motors
        for currentRow in range(int(c.numHiddenNeurons / 2)):
            for currentColumn in range(c.numBots * c.numMotorNeurons):
                sourceNeuron = neuronDict['HiddenHive']['startIndex'] + currentRow
                targetNeuron = neuronDict['Motor']['startIndex'] + currentColumn
                pyrosim.Send_Synapse(sourceNeuronName=sourceNeuron,
                                     targetNeuronName=targetNeuron,
                                     weight=hiddenHiveMotor[currentRow][currentColumn])

        # HiddenLocal to Motors
        for currentRow in range(int(c.numHiddenNeurons / 2)):
            for currentColumn in range(c.numBots * c.numMotorNeurons):
                sourceNeuron = neuronDict['HiddenLocal']['startIndex'] + currentRow
                targetNeuron = neuronDict['Motor']['startIndex'] + currentColumn
                pyrosim.Send_Synapse(sourceNeuronName=sourceNeuron,
                                     targetNeuronName=targetNeuron,
                                     weight=hiddenLocalMotor[currentRow][currentColumn])

        # Recurrant Hive connections
        for currentColumn in range(int(c.numHiddenNeurons / 2)):
            neuron = neuronDict['HiddenHive']['startIndex'] + currentColumn
            pyrosim.Send_Synapse(sourceNeuronName=neuron,
                                 targetNeuronName=neuron,
                                 weight=recurrantHive[0][currentColumn])

        # Recurrant Local connections
        for currentRow in range(c.numBots):
            for currentColumn in range(int(c.numHiddenNeurons / 2)):
                neuron = neuronDict['HiddenLocal']['startIndex'] + currentColumn
                pyrosim.Send_Synapse(sourceNeuronName=neuron,
                                     targetNeuronName=neuron,
                                     weight=recurrantLocal[currentRow][currentColumn])

    endingIndex = pyrosim.End()
