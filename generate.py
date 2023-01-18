# this file will use pyrosim to create a link
# Store it in a file called world.sdf
# read and simulate this file

import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")  # Creates file where world info will be stored

length = 1
width = 1
height = 1

x = 0
y = 0
z = 0.5

num_blocks = 10

for i in range(num_blocks):
    # Creates a cube and sends it to box. Units are in meters.
    pyrosim.Send_Cube(name='box', pos=[x, y, z + i], size=[length*(.9**i), width*(.9**i), height])


pyrosim.End()  # Close sdf file
