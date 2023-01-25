import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np  # For arrays to store sensor values
import random  # For randomized Motor control
import constants as c  # File in which we store many of the constants we are using

"""Class Imports"""
from simulation import SIMULATION
simulation = SIMULATION()

# physicsClient = p.connect(p.GUI)
# p.setAdditionalSearchPath(pybullet_data.getDataPath())  # Location for many built-in files
#
# # Set Gravity
# p.setGravity(c.X_GRAV, c.Y_GRAV, c.Z_GRAV)  # Set gravity downward gravitational pull
#
# p.loadURDF(c.PLANE)
# robotID = p.loadURDF(c.BOT_1)
# p.loadSDF(c.WORLD)
#
# pyrosim.Prepare_To_Simulate(robotID)  # Extra little work to have sensors set up for this robot
# # Would need to iterate through an array of robots if you wanted a swarm
#
# backLegSensorValues = np.zeros(c.SIM_LEN)
# frontLegSensorValues = np.zeros(c.SIM_LEN)
#
# # Create motor schedule for bot limbs
# back_x = np.linspace(start=0-c.BACK_PHASE, stop=2*np.pi-c.BACK_PHASE, num=c.FRAMES)*c.BACK_FREQ
# targetAnglesBack = np.sin(back_x)*c.BACK_AMP
#
# front_x = np.linspace(start=0-c.FRONT_PHASE, stop=2*np.pi-c.FRONT_PHASE, num=c.FRAMES)*c.FRONT_FREQ
# targetAnglesFront = np.sin(front_x)*c.FRONT_AMP
#
# np.save('data/targetAnglesBack.npy', targetAnglesBack)
# np.save('data/targetAnglesFront.npy', targetAnglesFront)
#
# for i in range(c.SIM_LEN):
#     p.stepSimulation()
#     #backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
#     pyrosim.Set_Motor_For_Joint(bodyIndex=robotID,
#                                 jointName="Torso_BackLeg",
#                                 controlMode=p.POSITION_CONTROL,
#                                 targetPosition=targetAnglesBack[i % c.FRAMES],
#                                 maxForce=c.BACK_FORCE)
#     #frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
#     pyrosim.Set_Motor_For_Joint(bodyIndex=robotID,
#                                 jointName="Torso_FrontLeg",
#                                 controlMode=p.POSITION_CONTROL,
#                                 targetPosition=targetAnglesFront[i % c.FRAMES],
#                                 maxForce=c.FRONT_FORCE)
#     time.sleep(c.SLEEP_TIME)
#
# #np.save('./data/backLegSensorValues.npy', backLegSensorValues)
# #np.save('./data/FrontLegSensorValues.npy', frontLegSensorValues)
# p.disconnect()