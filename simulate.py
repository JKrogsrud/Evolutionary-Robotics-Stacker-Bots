"""Class Imports"""
import time

from simulation import SIMULATION
import sys

directOrGUI = sys.argv[1]
solutionID = sys.argv[2]
bodyType = sys.argv[3]
numBots = sys.argv[4]

#
# directOrGUI = "GUI"
# solutionID = 0
# bodyType = 'A'
# numBots = 3
time.sleep(100)
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

