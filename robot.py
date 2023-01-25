import pybullet as p
import constants as c

class ROBOT:

    def __init__(self):
        self.sensors = {}
        self.motors = {}
        self.robotID = p.loadURDF(c.BOT_1)

