import numpy as np

"""SIMULATION CONSTANTS"""
SLEEP_TIME = 1/240
FRAMES = 1000

"""DATA COLLECTION"""
SIM_LEN = 1000

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
numSensorNeurons = 23
numHiddenNeurons = 20
numMotorNeurons = 16

totalNeurons = numSensorNeurons + numHiddenNeurons + numMotorNeurons

"""
Evolution Constants
"""
numberOfGenerations = 1
populationSize = 1

"""
Body experimentation
"""
bodytype = "A"
numBots = 1

if bodytype == 'A':
    topFlapSensorOffset = .43
    bottomFlapSensorOffset = .50
    torsoHeight = .20
    torsoSensorHeight = .2
    torsoSensorSize = .5

    # joint limitations
    # These should be a lower and upper bound for each joint
    # Neuron Values range between -1 and 1
    motorJointRanges = {
        'Torso_FrontFlap': (-1, -0.5),
        'Torso_BackFlap': (0.5, 1),
        'Torso_RightFlap': (0.5, 1),
        'Torso_LeftFlap': (-1, -0.5),
        'Torso_URRotate': (0.6, 1.2),
        'URRotate_URTopLeg': (-.75, -0.35),
        'URTopLeg_URBottomLeg': (-.75, -0.35),
        'Torso_ULRotate': (-1.2, -0.6),
        'ULRotate_ULTopLeg': (-.75, -0.35),
        'ULTopLeg_ULBottomLeg': (-.75, -0.35),
        'Torso_BRRotate': (0.6, 1.2),
        'BRRotate_BRTopLeg': (0.35, .75),
        'BRTopLeg_BRBottomLeg': (0.35, .75),
        'Torso_BLRotate': (-1.2, -0.6),
        'BLRotate_BLTopLeg': (0.35, .75),
        'BLTopLeg_BLBottomLeg': (0.35, .75),
    }

"""
Bot Spawning
types: horizontal, stacked
"""
startPos = 'horizontal'
# startPos = 'stacked'

if startPos == 'horizontal':
    botSpacing = 6
else:
    botSpacing = 7

"""
Data Reporting
"""
senseTiming = 50