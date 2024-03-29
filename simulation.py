import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import time

# My own created classes
from world import WORLD
from robot import ROBOTSWARM
from robot import HIVE_MIND

import constants as c  # File in which we store many of the constants we are using


class SIMULATION:
    def __init__(self, directOrGUI, solutionID, bodyType, numBots):
        # print("simulation constructor")
        self.directOrGui = directOrGUI
        self.bodyType = bodyType
        self.numBots = numBots

        if (directOrGUI == "DIRECT"):
            self.physicsClient = p.connect(p.DIRECT)
        else:
            self.physicsClient = p.connect(p.GUI)

        p.setAdditionalSearchPath(pybullet_data.getDataPath())  # Location for many built-in files
        p.setGravity(c.X_GRAV, c.Y_GRAV, c.Z_GRAV)

        self.world = WORLD()

        # Creating robots all in one file to fix sensor issues
        if c.BRAIN_TYPE in {'hive_mind', 'hive_mind_recurrant', 'hive_mind_recurrant_hybrid_A',
                            'hive_mind_recurrant_hybrid_B'}:
            self.robots = HIVE_MIND(solutionID, bodyType, self.numBots)
        else:
            self.robots = ROBOTSWARM(solutionID, bodyType, self.numBots)


    def run(self):
        for t in range(c.SIM_LEN):
            p.stepSimulation()
            if self.directOrGui == "GUI":
                time.sleep(c.SLEEP_TIME)

            # This is currently commented out because I've added recording to run_simulation
            # probably could be done a little bit more nicely

            # self.robots.Sense(t)

            self.robots.Think(t)
            self.robots.Act(t)

    def __del__(self):
        # self.robot.Save_Values()
        p.disconnect()

    def Get_Fitness(self):
        self.robots.Get_Fitness()
