import pybullet as p
import time
import pybullet_data

import pyrosim.pyrosim as pyrosim

import numpy  # For arrays to store sensor values

import random # For randomized Motor control

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())  # Location for many built-in files

p.setGravity(0, 0, -9.8)  # Set gravity downward gravitational pull

p.loadURDF("plane.urdf")

robotID = p.loadURDF("body.urdf")

p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotID)  # Extra little work to have sensors set up for this robot
# Would need to iterate through an array of robots if you wanted a swarm

backLegSensorValues = numpy.zeros(2000)
frontLegSensorValues = numpy.zeros(2000)

for i in range(2000):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    pyrosim.Set_Motor_For_Joint(bodyIndex=robotID,
                                jointName="Torso_BackLeg",
                                controlMode=p.POSITION_CONTROL,
                                targetPosition=random.random()*numpy.pi - numpy.pi/2,
                                maxForce=100)
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    pyrosim.Set_Motor_For_Joint(bodyIndex=robotID,
                                jointName="Torso_FrontLeg",
                                controlMode=p.POSITION_CONTROL,
                                targetPosition=random.random()*numpy.pi - numpy.pi/2,
                                maxForce=100)
    time.sleep(1/60)

numpy.save('./data/backLegSensorValues.npy', backLegSensorValues)
numpy.save('./data/FrontLegSensorValues.npy', frontLegSensorValues)
p.disconnect()