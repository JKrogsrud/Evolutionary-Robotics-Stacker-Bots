"""Class Imports"""
from simulation import SIMULATION
import sys

print("Here i am in simulate for args")

directOrGUI = sys.argv[1]
solutionID = sys.argv[2]
bodyType = sys.argv[3]
numBots = sys.argv[4]

print("here")

simulation = SIMULATION(directOrGUI, solutionID, bodyType, numBots)

simulation.run()

# simulation.Get_Fitness()

