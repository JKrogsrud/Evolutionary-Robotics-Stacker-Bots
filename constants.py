import numpy as np

"""SIMULATION CONSTANTS"""
SLEEP_TIME = 1/250

"""DATA COLLECTION"""
SIM_LEN = 100000

"""GRAVITY CONSTANTS"""
X_GRAV = 0
Y_GRAV = 0
Z_GRAV = -9.8

"""
BOT CONSTANTS
"""
# Frame repetition
FRAMES = 1000

"""
Bot Motion
types: ragdoll, oscillatory, randomNN, distributiveNN, hivemind
"""

# MOTION_TYPE = 'oscillatory'
# MOTION_TYPE = 'ragdoll'
MOTION_TYPE = 'rigid'

"""
MOTOR CONSTANTS - Oscillatory
"""
# random determines if the values for oscillation should be randomized or not
# RANDOM = True
RANDOM = False

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
    #TODO: Working on rigid body
    pass

"""
Neural Network
"""
numSensorNeurons = 9
numMotorNeurons = 8

"""
Evolution Constants
"""
numberOfGenerations = 10
populationSize = 10

"""
Body experimentation
"""
bodytype = "A"
numBots = 3

if bodytype == 'A':
    topFlapSensorOffset = .45
    bottomFlapSensorOffset = .55
    torsoHeight = .20
    torsoSensorHeight = .15
    torsoSensorSize = .75
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