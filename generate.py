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

    # length = 1
    # width = 1
    # height = 1
    #
    # x = 0
    # y = 0
    # z = 0.5
    #
    # pyrosim.Send_Cube(name='Link0', pos=[x, y, z], size=[length, width, height])
    # pyrosim.Send_Joint(name="Link0_Link1", parent="Link0", child="Link1", type="revolute",
    #                    position=[0, 0, 1])
    # pyrosim.Send_Cube(name='Link1', pos=[0, 0, 0.5], size=[length, width, height])
    # pyrosim.Send_Joint(name="Link1_Link2", parent="Link1", child="Link2", type="revolute",
    #                    position=[0, 0, 1])
    # pyrosim.Send_Cube(name='Link2', pos=[0, 0, 0.5], size=[length, width, height])
    # pyrosim.Send_Joint(name="Link2_Link3", parent="Link2", child="Link3", type="revolute",
    #                    position=[0, 0.5, 0.5])
    # pyrosim.Send_Cube(name='Link3', pos=[0, 0.5, 0], size=[length, width, height])
    # pyrosim.Send_Joint(name="Link3_Link4", parent="Link3", child="Link4", type="revolute",
    #                    position=[0, 1, 0])
    # pyrosim.Send_Cube(name='Link4', pos=[0, 0.5, 0], size=[length, width, height])
    # pyrosim.Send_Joint(name="Link4_Link5", parent="Link4", child="Link5", type="revolute",
    #                    position=[0, 0.5, -0.5])
    # pyrosim.Send_Cube(name='Link5', pos=[0, 0, -0.5], size=[length, width, height])
    # pyrosim.Send_Joint(name="Link5_Link6", parent="Link5", child="Link6", type="revolute",
    #                    position=[0, 0, -1])
    # pyrosim.Send_Cube(name='Link6', pos=[0, 0, -0.5], size=[length, width, height])

    pyrosim.Send_Cube(name='Torso', pos=[1.5, 0, 1.5], size=[1, 1, 1])
    pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute",
                       position=[1, 0, 1])
    pyrosim.Send_Cube(name='BackLeg', pos=[-0.5, 0, -0.5], size=[1, 1, 1])
    pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute",
                       position=[2, 0, 1])
    pyrosim.Send_Cube(name='FrontLeg', pos=[0.5, 0, -0.5], size=[1, 1, 1])

    pyrosim.End()  # Close sdf file


create_world()
create_robot()