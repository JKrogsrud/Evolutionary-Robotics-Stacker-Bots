"""Class Imports"""
import time

from simulation import SIMULATION
import sys

directOrGUI = sys.argv[1]
solutionID = sys.argv[2]
bodyType = sys.argv[3]
numBots = sys.argv[4]

simulation = SIMULATION(directOrGUI, solutionID, bodyType, numBots)
simulation.run()
simulation.Get_Fitness()


