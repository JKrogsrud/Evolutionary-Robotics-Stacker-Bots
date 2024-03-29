import os
from solution import SOLUTION
import constants as c
import copy as cp

class SURVIVE_MULTIPLY:

    def __init__(self, bodyType, numBots):

        os.system("del brain*.nndf")
        os.system("del fitness*.nndf")
        os.system("del best*.nndf")

        self.parents = {}

        self.nextAvailableID = 0

        for parent in range(c.populationSize):
            self.parents[parent] = SOLUTION(self.nextAvailableID, bodyType, numBots)
            self.nextAvailableID += 1

    def Evolve(self):

        self.Evaluate(self.parents)

        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()

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

    # Helper function for Select
    def find_lowest(self, solutions: dict[int, SOLUTION]) -> int:
        lowest_key = None
        lowest_fitness = 999999
        for sol in solutions:
            if solutions[sol].fitness < lowest_fitness:
                lowest_key = sol
                lowest_fitness = solutions[sol].fitness
        return lowest_key


    def Select(self):
        lowest_parent = self.find_lowest(self.parents)
        lowest_fitness = self.parents[lowest_parent].fitness
        for child in self.children:
            if self.children[child].fitness > lowest_fitness:
                self.parents[lowest_parent] = self.children[child]
            lowest_parent = self.find_lowest(self.parents)
            lowest_fitness = self.parents[lowest_parent].fitness


        # all_solutions = dict(self.parents.items() | self.children.items())
        # print(all_solutions)
        # sorted_by_fitness = sorted(all_solutions.items(), key=lambda x: x[1].fitness)
        # survivors = sorted_by_fitness[-int(c.populationSize):]
        #
        # # I now have half the winners
        # # Lets throw them back into
        # parent_tmp = {}
        # for i in range(len(survivors)):
        #     parent_tmp[i] = survivors[i][1]
        #
        # self.parents = parent_tmp
    def Print(self):
        for parent in self.parents:
            print("Parent " + str(parent) + "'s fitness:" + str(self.parents[parent].fitness) +
                  ", Child: " + str(self.children[parent].fitness))

    def Save_Best(self):
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
        if c.BRAIN_TYPE in {'hive_mind', 'hive_mind_recurrant', 'hive_mind_recurrant_hybrid_A',
                            'hive_mind_recurrant_hybrid_B'}:
            os.rename('brain_' + str(IDofFittest) + str(c.bodytype) + '.nndf', 'best_brain.nndf')
        else:
            for botNum in range(c.numBots):
                os.rename('brain_' + str(IDofFittest) + str(c.bodytype) + str(botNum) + '.nndf',
                        'best_brain_' + str(botNum) + '.nndf')

        # create and save a .csv file with helpful info



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