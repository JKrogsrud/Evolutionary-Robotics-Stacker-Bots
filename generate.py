# this file will use pyrosim to create a link
# Store it in a file called world.sdf
# read and simulate this file

import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("world.sdf")  # Creates file where world info will be stored

length = 2
width = 2
height = 2

x = 0
y = 0
z = height/2

pyrosim.Send_Cube(name='box', pos=[x, y, z], size=[length, width, height])

pyrosim.End()  # Close sdf file
