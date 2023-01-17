import pybullet as p
import time

physicsClient = p.connect(p.GUI)

for i in range(2000):
    p.stepSimulation()
    time.sleep(1/60)
    print(i)

p.disconnect()