import pybullet as p
import time
import pybullet_data

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())  # Location for many built-in files

p.setGravity(0, 0, -9.8)  # Set gravity downward gravitational pull

p.loadURDF("plane.urdf")

p.loadSDF("boxes.sdf")

for i in range(10000):
    p.stepSimulation()
    time.sleep(1/120)
    print(i)

p.disconnect()