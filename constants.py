import numpy as np

"""SIMULATION CONSTANTS"""
SLEEP_TIME = 1/250

"""DATA COLLECTION"""
SIM_LEN = 2

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
MOTOR CONSTANTS - Oscillatory
"""

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
numBots = 2

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
Bot Motion
types: ragdoll, oscillatory, randomNN, distributiveNN, hivemind
"""

# MOTION_TYPE = 'oscillatory'
MOTION_TYPE = 'ragdoll'

"""
Data Reporting
"""
senseTiming = 1