import numpy as np

"""SIMULATION CONSTANTS"""
SLEEP_TIME = 1/240

"""ROBOT, PLANE and WORLD filenames"""
PLANE = "plane.urdf"
BOT_1 = "body.urdf"
WORLD = "world.sdf"

"""DATA COLLECTION"""
SIM_LEN = 5000

"""GRAVITY CONSTANTS"""
X_GRAV = 0
Y_GRAV = 0
Z_GRAV = -9.8

"""
BOT CONSTANTS
"""
# Frame repetition
FRAMES = 1000

# Back Leg values
BACK_AMP = 4 * np.pi / 16
BACK_FREQ = 6.1
BACK_PHASE = -4 * np.pi / 16
BACK_FORCE = 100

# Front Leg Values
FRONT_AMP = 3 * np.pi / 16
FRONT_FREQ = 6.1
FRONT_PHASE = 0
FRONT_FORCE = 100
