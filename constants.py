import numpy as np

"""SIMULATION CONSTANTS"""
SLEEP_TIME = 1/240
FRAMES = 1000

"""DATA COLLECTION"""
SIM_LEN = 5000

"""GRAVITY CONSTANTS"""
X_GRAV = 0
Y_GRAV = 0
Z_GRAV = -9.8

"""
BOT CONSTANTS
"""

MAX_FORCE = 100

"""
Bot Motion
types: neural_network, hive_mind
"""

BRAIN_TYPE = 'neural_network'
# BRAIN_TYPE = 'hive_mind'

"""
Evolution Constants
"""

numberOfGenerations = 1
populationSize = 2

# evolutionaryAlgorithm = 'PHC'
evolutionaryAlgorithm = 'SAM'

"""
Fitness
"""

# fitness = 'top_sensor_1'
fitness = 'gather_and_stack'

# For the top_sensor:
if fitness == 'top_sensor_1':
    goal = (0, 0)
    goalDistance = 2
    targetFrames = 10  # as a percent at end of run
    sensorFitnessMultiplier = 1
    flipPenalty = 1
    gatherFitnessMultiplier = 1

if fitness == 'gather_and_stack':
    goal = (0, 0)
    goalDistance = 1

    distanceFitnessWeight = 3
    sensorFitnessWeight = 1
    dormancyFitnessWeight = 1


"""
Body experimentation
"""
bodytype = "A"
numBots = 3  # Limit to 9 - or need to rethink something in Robot - Act

motors = [
        ('Torso', 'URRotate'), ('URRotate', 'URTopLeg'), ('URTopLeg', 'URBottomLeg'),
        ('Torso', 'ULRotate'), ('ULRotate', 'ULTopLeg'), ('ULTopLeg', 'ULBottomLeg'),
        ('Torso', 'BRRotate'), ('BRRotate', 'BRTopLeg'), ('BRTopLeg', 'BRBottomLeg'),
        ('Torso', 'BLRotate'), ('BLRotate', 'BLTopLeg'), ('BLTopLeg', 'BLBottomLeg')]

# Outdated Motors:
"""
('Torso', 'FrontFlap'), ('Torso', 'BackFlap'), ('Torso', 'RightFlap'), ('Torso', 'LeftFlap')
"""

cube_sensors = [
        'TopSensor', 'BottomSensor',
        'URBottomLeg', 'ULBottomLeg', 'BRBottomLeg',
        'BLBottomLeg']

# Outdated Sensors:
"""
'FrontTopSensor', 'FrontBottomSensor',
'BackTopSensor', 'BackBottomSensor', 'RightTopSensor',
'RightBottomSensor', 'LeftTopSensor', 'LeftBottomSensor',
"""


"""
Neural Network
"""

# Neurons
numSensorNeurons = len(cube_sensors)
numHiddenNeurons = 10
numMotorNeurons = len(motors)

totalNeurons = numSensorNeurons + numHiddenNeurons + numMotorNeurons

# Synaptic weight intialization
mu = 0
sigma = 1/3

"""
Body Constants
"""

# First bodytype - probably last too
if bodytype == 'A':
    topFlapSensorOffset = .43
    bottomFlapSensorOffset = .50
    torsoHeight = .20
    torsoSensorHeight = .2
    torsoSensorSize = .5

    # joint limitations
    # These should be a lower and upper bound for each joint
    # Neuron Values range between -1 and 1

    """
    Rotate joints: 
    """

    motorJointRanges = {
        'Torso_URRotate': (0, np.pi / 2),
        'URRotate_URTopLeg': (-np.pi / 3, np.pi / 4),
        'URTopLeg_URBottomLeg': (-np.pi / 2 - np.pi / 16, -np.pi / 4),
        'Torso_ULRotate': (-np.pi / 2, 0),
        'ULRotate_ULTopLeg': (-np.pi / 3, np.pi / 4),
        'ULTopLeg_ULBottomLeg': (-np.pi / 2 - np.pi / 16, -np.pi / 4),
        'Torso_BRRotate': (0, np.pi / 2),
        'BRRotate_BRTopLeg': (-np.pi / 4, np.pi / 3),
        'BRTopLeg_BRBottomLeg': (np.pi / 4, np.pi / 2 + np.pi / 16),
        'Torso_BLRotate': (-np.pi / 2, 0),
        'BLRotate_BLTopLeg': (-np.pi / 4, np.pi / 3),
        'BLTopLeg_BLBottomLeg': (np.pi / 4, np.pi / 2 + np.pi / 16),
    }

    """
    Dormant output
    """
    dormantMotorJointValues = {
        'Torso_URRotate': np.pi / 4,
        'URRotate_URTopLeg': 0,
        'URTopLeg_URBottomLeg': np.pi / 12,
        'Torso_ULRotate': -np.pi / 4,
        'ULRotate_ULTopLeg': 0,
        'ULTopLeg_ULBottomLeg': np.pi / 12,
        'Torso_BRRotate': np.pi / 4,
        'BRRotate_BRTopLeg': 0,
        'BRTopLeg_BRBottomLeg': -np.pi / 12,
        'Torso_BLRotate': -np.pi / 4,
        'BLRotate_BLTopLeg': 0,
        'BLTopLeg_BLBottomLeg': -np.pi / 12,
    }

### Colors ###

DEFAULT = ("DEFAULT", 0/255.0, 204.0/255.0, 204.0 / 255.0, 1.0)

# Red
UR = ("UR", 255.0/255.0, 0/255.0, 0 / 255.0, 1.0)
# White
BR = ("BR", 255.0/255.0, 255.0/255.0, 255.0 / 255.0, 1.0)
# Blue
UL = ("UL", 0/255.0, 0/255.0, 200.0 / 255.0, 1.0)
# Green
BL = ("BL", 0/255.0, 255.0/255.0, 0.0 / 255.0, 1.0)

"""
Bot Spawning
types: horizontal, stacked
"""
# startPos = 'horizontal'
# startPos = 'stacked'
startPos = 'circle'

if startPos == 'circle':
    startRadius = 7

if startPos == 'horizontal':
    botSpacing = 5.5
else:
    botSpacing = 7

"""
Data Reporting
"""
senseTiming = 50