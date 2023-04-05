import numpy as np

"""SIMULATION CONSTANTS"""
SLEEP_TIME = 1/240
FRAMES = 1000

"""DATA COLLECTION"""
SIM_LEN = 10000

"""GRAVITY CONSTANTS"""
X_GRAV = 0
Y_GRAV = 0
Z_GRAV = -9.8

"""
BOT CONSTANTS
"""
# Frame repetition
MAX_FORCE = 100

"""
Bot Motion
types: ragdoll, oscillatory, randomNN, neural_network
"""

# MOTION_TYPE = 'oscillatory'
MOTION_TYPE = 'neural_network'
# MOTION_TYPE = 'ragdoll'
# MOTION_TYPE = 'rigid'

"""
MOTOR CONSTANTS - Oscillatory
"""
# random determines if the values for oscillation should be randomized or not
RANDOM = True
# RANDOM = False

# Set true to test bot 1 not behaving at all
# DIFFERENT_BEHAVIOR = True
DIFFERENT_BEHAVIOR = False

"""
MOTOR RANGES 
"""
if RANDOM == True and MOTION_TYPE == 'oscillatory':
    # Flaps
    FLAP_AMPS = np.random.random_sample() * 2 * np.pi
    FLAP_FREQ = np.random.random_sample() * 10.0
    FLAP_OFFSET = - np.random.random_sample() * np.pi / 3
    FLAP_TRANSLATION = - np.random.random_sample() * np.pi / 3

    # ROTATORS
    ROTATOR_AMPS = np.random.random_sample() * np.pi / 2
    ROTATOR_FREQ = np.random.random_sample() * 10.0
    ROTATOR_OFFSET = - np.random.random_sample() * np.pi / 2
    ROTATOR_TRANSLATION = np.random.random_sample() * np.pi / 2

    # LEGS
    # Upper Leg
    UPPER_LEG_AMPS = np.random.random_sample() * np.pi / 4
    UPPER_LEG_FREQ = np.random.random_sample() * 10.0
    UPPER_LEG_OFFSET = - np.random.random_sample() * np.pi / 3
    UPPER_LEG_TRANSLATION = np.random.random_sample() * np.pi / 3

    # Lower Leg
    LOWER_LEG_AMPS = np.random.random_sample() * np.pi / 4
    LOWER_LEG_FREQ = np.random.random_sample() * 10.0
    LOWER_LEG_OFFSET = -np.random.random_sample() * np.pi / 3
    LOWER_LEG_TRANSLATION = np.random.random_sample() * np.pi / 3

    # Motor Force
    MAX_FORCE = 100

    # Joint Restrictions
    motorJointRange = np.random.random_sample()

elif RANDOM == False and MOTION_TYPE == 'oscillatory':
    # FLAPS
    FLAP_AMPS = 3 * np.pi / 16
    FLAP_FREQ = 6.1
    FLAP_OFFSET = - np.pi / 4
    FLAP_TRANSLATION = - np.pi / 4

    # ROTATORS
    ROTATOR_AMPS = np.pi / 4
    ROTATOR_FREQ = 6.1
    ROTATOR_OFFSET = - np.pi / 4
    ROTATOR_TRANSLATION = np.pi /4

    # LEGS
    # Upper Leg
    UPPER_LEG_AMPS = np.pi / 6
    UPPER_LEG_FREQ = 6.1
    UPPER_LEG_OFFSET = -np.pi / 5
    UPPER_LEG_TRANSLATION = 0

    # Lower Leg
    LOWER_LEG_AMPS = np.pi / 4
    LOWER_LEG_FREQ = 6.1
    LOWER_LEG_OFFSET = -np.pi / 2
    LOWER_LEG_TRANSLATION = np.pi / 3

    # Motor Force
    MAX_FORCE = 100

    # Joint Restrictions
    motorJointRange = 0.4

elif MOTION_TYPE == 'rigid':

    TORSO_FLAP_ANGLE = np.pi / 3.5

    ROTATOR_ANGLE = np.pi / 4

    TOP_LEG_ANGLE = np.pi / 7

    BOTTOM_LEG_ANGLE = np.pi / 2.1

    MAX_FORCE = 100

"""
Neural Network
"""
# numSensorNeurons = 23
numSensorNeurons = 14
# numHiddenNeurons = 20
numHiddenNeurons = 14
numMotorNeurons = 16

totalNeurons = numSensorNeurons + numHiddenNeurons + numMotorNeurons

"""
Evolution Constants
"""
numberOfGenerations = 250
populationSize = 5

"""
Body experimentation
"""
bodytype = "A"
numBots = 2

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
        'Torso_FrontFlap': (-np.pi / 4 - 0.1, 0),
        'Torso_BackFlap': (0, np.pi / 4 + 0.1),
        'Torso_RightFlap': (0, np.pi / 4 + 0.1),
        'Torso_LeftFlap': (-np.pi / 4 - 0.1, 0),
        'Torso_URRotate': (0, np.pi / 2),
        'URRotate_URTopLeg': (-np.pi / 3, np.pi / 4),
        'URTopLeg_URBottomLeg': (-np.pi / 2, 0),
        'Torso_ULRotate': (-np.pi / 2, 0),
        'ULRotate_ULTopLeg': (-np.pi / 3, np.pi / 4),
        'ULTopLeg_ULBottomLeg': (-np.pi / 2, 0),
        'Torso_BRRotate': (0, np.pi / 2),
        'BRRotate_BRTopLeg': (-np.pi / 4, np.pi / 3),
        'BRTopLeg_BRBottomLeg': (0, np.pi / 2),
        'Torso_BLRotate': (-np.pi / 2, 0),
        'BLRotate_BLTopLeg': (-np.pi / 4, np.pi / 3),
        'BLTopLeg_BLBottomLeg': (0, np.pi / 2),
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
startPos = 'horizontal'
# startPos = 'stacked'

if startPos == 'horizontal':
    botSpacing = 5.5
else:
    botSpacing = 7

"""
Data Reporting
"""
senseTiming = 50