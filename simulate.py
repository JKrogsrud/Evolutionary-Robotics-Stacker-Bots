import pybullet as p
import time
import pybullet_data

import pyrosim.pyrosim as pyrosim

import numpy as np  # For arrays to store sensor values

import random  # For randomized Motor control

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())  # Location for many built-in files

p.setGravity(0, 0, -9.8)  # Set gravity downward gravitational pull

p.loadURDF("plane.urdf")

robotID = p.loadURDF("body.urdf")

p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotID)  # Extra little work to have sensors set up for this robot
# Would need to iterate through an array of robots if you wanted a swarm

backLegSensorValues = np.zeros(1000)
frontLegSensorValues = np.zeros(1000)

x = np.linspace(start=0, stop=2*np.pi, num=1000)

targetAnglesBack = np.sin(x)*np.pi/4
targetAnglesFront = np.sin(x)*np.pi/4

np.save('data/targetAngles.npy', targetAnglesBack)

for i in range(2000):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    pyrosim.Set_Motor_For_Joint(bodyIndex=robotID,
                                jointName="Torso_BackLeg",
                                controlMode=p.POSITION_CONTROL,
                                targetPosition=targetAnglesBack[i % 2000],
                                maxForce=100)
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    pyrosim.Set_Motor_For_Joint(bodyIndex=robotID,
                                jointName="Torso_FrontLeg",
                                controlMode=p.POSITION_CONTROL,
                                targetPosition=targetAnglesFront[i % 2000],
                                maxForce=100)
    time.sleep(1/60)

np.save('./data/backLegSensorValues.npy', backLegSensorValues)
np.save('./data/FrontLegSensorValues.npy', frontLegSensorValues)
p.disconnect()