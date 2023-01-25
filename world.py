import pybullet as p
import constants as c
import pybullet_data.data

class WORLD:
    def __int__(self):
        p.loadURDF("plane.urdf")
        p.loadSDF("world.sdf")
