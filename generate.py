# this file will use pyrosim to create a link
# Store it in a file called world.sdf
# read and simulate this file

import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("box.sdf")  # Creates file where world info will be stored

length = 1
width = 2
height = 3

x = 0
y = 0
z = 1.5

# Creates a cube and sends it to box. Units are in meters.
pyrosim.Send_Cube(name='box', pos=[x, y, z], size=[length, width, height])

pyrosim.End()  # Close sdf file
