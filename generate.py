# this file will use pyrosim to create a link
# Store it in a file called world.sdf
# read and simulate this file

import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("box.sdf")  # Creates file where world info will be stored

length = 1
width = 2
height = 3

# Creates a cube and sends it to box. Units are in meters.
pyrosim.Send_Cube(name='box', pos=[0, 0, 0.5], size=[length, width, height])

pyrosim.End()  # Close sdf file
