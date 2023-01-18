# this file will use pyrosim to create a link
# Store it in a file called world.sdf
# read and simulate this file

import pyrosim.pyrosim as pyrosim


def create_world():
    pyrosim.Start_SDF("world.sdf")  # Creates file where world info will be stored

    length = 2
    width = 2
    height = 2

    x = -4
    y = 4
    z = height/2

    pyrosim.Send_Cube(name='box', pos=[x, y, z], size=[length, width, height])

    pyrosim.End()  # Close sdf file


def create_robot():
    pyrosim.Start_URDF("body.urdf")

    length = 1
    width = 1
    height = 1

    x = 0
    y = 0
    z = 0.5

    pyrosim.Send_Cube(name='Link1', pos=[x, y, z], size=[length, width, height])
    pyrosim.Send_Joint(name="Link1_Link2", parent="Link1", child="Link2", type="revolute",
                       position=[0.5, 0, 1])
    pyrosim.Send_Cube(name='Link2', pos=[0.5, 0, 0.5], size=[length, width, height])

    pyrosim.End()  # Close sdf file


create_world()
create_robot()