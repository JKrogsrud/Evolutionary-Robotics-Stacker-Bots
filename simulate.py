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

# Some values to help with motor control
back_amplitude = 4*np.pi/16
back_frequency = 6.1
back_phaseOffset = -4*np.pi/16

back_x = np.linspace(start=0-back_phaseOffset, stop=2*np.pi-back_phaseOffset, num=1000)*back_frequency

targetAnglesBack = np.sin(back_x)*back_amplitude

front_amplitude = 3*np.pi/16
front_frequency = 6.1
front_phaseOffset = 0

front_x = np.linspace(start=0-front_phaseOffset, stop=2*np.pi-front_phaseOffset, num=1000)*front_frequency

targetAnglesFront = np.sin(front_x)*front_amplitude

np.save('data/targetAnglesBack.npy', targetAnglesBack)
np.save('data/targetAnglesFront.npy', targetAnglesFront)

for i in range(5000):
    p.stepSimulation()
    #backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    pyrosim.Set_Motor_For_Joint(bodyIndex=robotID,
                                jointName="Torso_BackLeg",
                                controlMode=p.POSITION_CONTROL,
                                targetPosition=targetAnglesBack[i % 1000],
                                maxForce=100)
    #frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    pyrosim.Set_Motor_For_Joint(bodyIndex=robotID,
                                jointName="Torso_FrontLeg",
                                controlMode=p.POSITION_CONTROL,
                                targetPosition=targetAnglesFront[i % 1000],
                                maxForce=100)
    time.sleep(1/240)

#np.save('./data/backLegSensorValues.npy', backLegSensorValues)
#np.save('./data/FrontLegSensorValues.npy', frontLegSensorValues)
p.disconnect()