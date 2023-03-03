"""Class Imports"""
from simulation import SIMULATION
import sys

directOrGUI = sys.argv[1]
solutionID = sys.argv[2]
bodyType = sys.argv[3]

simulation = SIMULATION(directOrGUI, solutionID, bodyType)

simulation.run()

# simulation.Get_Fitness()

