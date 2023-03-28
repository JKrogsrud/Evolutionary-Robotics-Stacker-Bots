import os

from solution import SOLUTION
import constants as c
import copy as cp
class PARALLEL_HILLCLIMBER:

    def __init__(self, bodyType, numBots):

        os.system("del brain*.nndf")
        os.system("del fitness*.nndf")

        # self.parents = {}

        self.nextAvailableID = 0
        print("in PHC:")

        # for parent in range(c.populationSize):
        #     self.parents[parent] = SOLUTION(self.nextAvailableID, bodyType, numBots)
        #     self.nextAvailableID += 1

        # For creation of a multiple bodies
        print("Calling SOLUTION:")
        self.solution = SOLUTION(self.nextAvailableID, bodyType, numBots)


    def Evolve(self):
        print("In evolve: calling evaluate")
        self.Evaluate(self.solution)

        # self.Evaluate(self.parents)
        # for currentGeneration in range(numberOfGenerations):
        #     self.Evolve_For_One_Generation()

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
        # if self.parent.fitness > self.child.fitness:
        #     self.parent = self.child
        for parent in self.parents:
            if self.parents[parent].fitness > self.children[parent].fitness:
                self.parents[parent] = self.children[parent]

    def Print(self):
        for parent in self.parents:
            print("Parent " + str(parent) + "'s fitness:" + str(self.parents[parent].fitness) +
                  ", Child: " + str(self.children[parent].fitness))

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

        print("In evaluate calling SOLUTION.Start_Simulation:")
        self.solution.Start_Simulation('GUI')

        # for solution in solutions:
        #     solutions[solution].Start_Simulation('DIRECT')
        # for solution in solutions:
        #     solutions[solution].Wait_For_Simulation_To_End()
