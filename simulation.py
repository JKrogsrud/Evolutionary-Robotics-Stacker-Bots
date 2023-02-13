import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import time

# My own created classes
from world import WORLD
from robot import ROBOT
# import generate # uncomment if you want to run generate automatically before simulate

import constants as c  # File in which we store many of the constants we are using


class SIMULATION:
    def __init__(self, directOrGUI):
        if (directOrGUI == "DIRECT"):
            self.physicsClient = p.connect(p.DIRECT)
        else:
            self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())  # Location for many built-in files
        p.setGravity(c.X_GRAV, c.Y_GRAV, c.Z_GRAV)

        self.world = WORLD()
        self.robot = ROBOT()

    def run(self):
        for t in range(c.SIM_LEN):
            p.stepSimulation()
            #time.sleep(c.SLEEP_TIME)
            self.robot.Sense()
            self.robot.Think()
            self.robot.Act()

    def __del__(self):
        # self.robot.Save_Values()
        p.disconnect()

    def Get_Fitness(self):
        self.robot.Get_Fitness()