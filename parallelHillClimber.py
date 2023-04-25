import os

import numpy as np

from solution import SOLUTION
import constants as c
import copy as cp
class PARALLEL_HILLCLIMBER:

    def __init__(self, bodyType, numBots):

        os.system("del brain*.nndf")
        os.system("del fitness*.nndf")
        os.system("del best*.nndf")

        self.fitnesses = np.zeros((c.populationSize, c.numberOfGenerations, c.numBots))
        self.fitnessPieces = np.zeros((c.populationSize, c.numberOfGenerations, c.numBots, 5))
        self.currentGeneration = 0
        self.parents = {}

        self.nextAvailableID = 0

        for parent in range(c.populationSize):
            self.parents[parent] = SOLUTION(self.nextAvailableID, bodyType, numBots)
            self.nextAvailableID += 1

    def Evolve(self):

        self.Evaluate(self.parents)

        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()
            self.currentGeneration += 1

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        print("---")
        self.Print()
        print("---")
        self.Select()


    def Spawn(self):
        self.children = {}
        for parent in range(len(self.parents)):
            self.children[parent] = cp.deepcopy(self.parents[parent])
            self.children[parent].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1


    def Mutate(self):
        for child in self.children:
            self.children[child].Mutate()

    def Select(self):
        parentNum = 0
        for parent in self.parents:
            # Here we can gather some data:
            botFitnesses = [fit[0] for fit in self.parents[parent].subFitness]

            # Individual bot fitnesses storage
            botNum = 0
            for vals in self.parents[parent].subFitness:
                self.fitnessPieces[parentNum][self.currentGeneration][botNum][:] = vals
                botNum += 1

            self.fitnesses[parentNum][self.currentGeneration][:] = botFitnesses
            if self.parents[parent].fitness < self.children[parent].fitness:
                self.parents[parent] = self.children[parent]
            parentNum += 1

    def Print(self):
        for parent in self.parents:
            print("Parent " + str(parent) + "'s fitness:" + str(self.parents[parent].fitness) +
                  ", Child: " + str(self.children[parent].fitness))

    def Save_Best(self):
        min_fit = 999
        fittest_parent = None
        for parent in self.parents:
            if fittest_parent is None:
                fittest_parent = parent
                min_fit = self.parents[parent].fitness
            else:
                if self.parents[parent].fitness < min_fit:
                    fittest_parent = parent
                    min_fit = self.parents[parent].fitness
        # self.parents[fittest_parent].Start_Simulation('GUI')
        # parent is a solution which is a number of robots, we want to save the brains
        # of the fittest solution:
        IDofFittest = self.parents[fittest_parent].myID

        if c.BRAIN_TYPE == 'hive_mind_recurrant':
            os.rename('brain_' + str(IDofFittest) + str(c.bodytype) + '.nndf',
                      'best_brain.nndf')
        else:
            for botNum in range(c.numBots):
                os.rename('brain_' + str(IDofFittest) + str(c.bodytype) + str(botNum) + '.nndf',
                        'best_brain_' + str(botNum) + '.nndf')

        # Save the fitnesses
        np.save('all_fitness', self.fitnesses)

        # Save the fitness pieces
        np.save('all_fitness_pieces', self.fitnessPieces)

    def Show_Best(self):
        # self.parent.Evaluate('GUI')
        min_fit = 999
        fittest_parent = None
        for parent in self.parents:
            if fittest_parent is None:
                fittest_parent = parent
                min_fit = self.parents[parent].fitness
            else:
                if self.parents[parent].fitness < min_fit:
                    fittest_parent = parent
                    min_fit = self.parents[parent].fitness
        self.parents[fittest_parent].Start_Simulation('GUI')

    def Evaluate(self, solutions):

        for solution in solutions:
            solutions[solution].Start_Simulation('DIRECT')
        for solution in solutions:
            solutions[solution].Wait_For_Simulation_To_End()


