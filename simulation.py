import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim

# My own created classes
from world import WORLD
from robot import ROBOT
import constants as c  # File in which we store many of the constants we are using


class SIMULATION:
    def __init__(self):

        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())  # Location for many built-in files
        p.setGravity(c.X_GRAV, c.Y_GRAV, c.Z_GRAV)

        self.world = WORLD()
        self.robot = ROBOT()

        pyrosim.Prepare_To_Simulate(self.world.worldID)
        pyrosim.Prepare_To_Simulate(self.world.planeID)
        pyrosim.Prepare_To_Simulate(self.robot.robotID)