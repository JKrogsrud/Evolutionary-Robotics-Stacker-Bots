import os

import numpy as np

from solution import SOLUTION
import constants as c
import copy as cp

class RANDOM_NETWORKS:

    def __init__(self, bodyType, numBots):

        os.system("del brain*.nndf")
        os.system("del fitness*.nndf")
        os.system("del best*.nndf")

        self.bodyType = bodyType
        self.numBots = numBots

        self.fitnesses = np.zeros((c.numGens, c.numBots))
        self.fitnessPieces = np.zeros((c.numGens, c.numBots, 5))
        self.currentGeneration = 0

        self.currentSolution = SOLUTION(self.currentGeneration, bodyType, numBots)

    def Evolve(self):

        self.Evaluate()

        for currentGeneration in range(c.numGens):
            self.Evolve_For_One_Generation()
            self.currentGeneration += 1

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Evaluate()
        self.Gather_Data()

    def Spawn(self):
        self.currentSolution = SOLUTION(self.currentGeneration, self.bodyType, self.numBots)

    def Evaluate(self):
        self.currentSolution.Start_Simulation('DIRECT')
        self.currentSolution.Wait_For_Simulation_To_End()

    def Gather_Data(self):
        botNum = 0
        for vals in self.currentSolution.subFitness:
            self.fitnessPieces[self.currentGeneration][botNum][:] = vals
            botNum += 1
        print(self.fitnessPieces)

    def Save(self):
        pass