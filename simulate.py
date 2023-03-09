"""Class Imports"""
from simulation import SIMULATION
import sys

# print("In Simulate: with args:")
#
directOrGUI = sys.argv[1]
solutionID = sys.argv[2]
bodyType = sys.argv[3]
numBots = sys.argv[4]
#
for i in range(5):
    print(sys.argv[i])

print("here")

simulation = SIMULATION(directOrGUI, solutionID, bodyType, numBots)
simulation.run()

# def run():
#     directOrGUI = 'GUI'
#     solutionID = 0
#     bodyType = 'A'
#     numBots = 3
#
#     simulation = SIMULATION(directOrGUI, solutionID, bodyType, numBots)
#
#     simulation.run()

# simulation.Get_Fitness()

