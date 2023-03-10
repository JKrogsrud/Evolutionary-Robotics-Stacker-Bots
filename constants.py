import numpy as np

"""SIMULATION CONSTANTS"""
SLEEP_TIME = 1/250

"""DATA COLLECTION"""
SIM_LEN = 25000

"""GRAVITY CONSTANTS"""
X_GRAV = 0
Y_GRAV = 0
# Z_GRAV = -9.8
Z_GRAV = -30

"""
BOT CONSTANTS
"""
# Frame repetition
FRAMES = 1000

# Back Leg values
BACK_AMP = 4 * np.pi / 16
BACK_FREQ = 6.1
BACK_PHASE = -4 * np.pi / 16

# Front Leg Values
FRONT_AMP = 3 * np.pi / 16
FRONT_FREQ = 6.1
FRONT_PHASE = 0

# Motor Force
MAX_FORCE = 100

# Joint Restrictions
motorJointRange = 0.4

# Neural Network
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
numBots = 5

"""
Bot Spawning
types: horizontal, stacked
"""
# startPos = 'horizontal'
startPos = 'stacked'

if startPos == 'horizontal':
    botSpacing = 6
else:
    botSpacing = 7