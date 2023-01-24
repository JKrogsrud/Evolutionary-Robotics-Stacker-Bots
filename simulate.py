import pybullet as p
import time
import pybullet_data

import pyrosim.pyrosim as pyrosim

import numpy  # For arrays to store sensor values

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())  # Location for many built-in files

p.setGravity(0, 0, -9.8)  # Set gravity downward gravitational pull

p.loadURDF("plane.urdf")

robotID = p.loadURDF("body.urdf")

p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotID)  # Extra little work to have sensors set up for this robot
# Would need to iterate through an array of robots if you wanted a swarm

backLegSensorValues = numpy.zeros(200)
frontLegSensorValues = numpy.zeros(200)

for i in range(200):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    time.sleep(1/60)
    #print(i)

numpy.save('./data/backLegSensorValues.npy', backLegSensorValues)
numpy.save('./data/FrontLegSensorValues.npy', frontLegSensorValues)
p.disconnect()