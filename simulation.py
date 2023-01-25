import pybullet as p

# My own created classes
from world import WORLD
from robot import ROBOT
import constants as c  # File in which we store many of the constants we are using


class SIMULATION:
    def __init__(self):
        self.world = WORLD()
        self.robot = ROBOT()
        self.physicsClient = p.connect(p.GUI)
