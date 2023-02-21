import os

from solution import SOLUTION
from constants import *
import copy as cp
class PARALLEL_HILLCLIMBER:

    def __init__(self):
        os.system("del brain*.nndf")
        os.system("del fitness*.nndf")
        self.parents = {}
        self.nextAvailableID = 0
        for parent in range(populationSize):
            self.parents[parent] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1


    def Evolve(self):
        for parent in self.parents:
            self.parents[parent].Start_Simulation('DIRECT')
        print("----")
        for parent in self.parents:
            self.parents[parent].Wait_For_Simulation_To_End()
        for currentGeneration in range(numberOfGenerations):
            self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        # self.Mutate()
        # self.child.Evaluate('DIRECT')
        # self.Print()
        # self.Select()
        pass


    def Spawn(self):
        self.children = {}
        for parent in range(len(self.parents)):
            self.children[parent] = cp.deepcopy(self.parents[parent])
            self.children[parent].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1


    def Mutate(self):
        self.child.Mutate()

    def Select(self):
        if self.parent.fitness > self.child.fitness:
            self.parent = self.child

    def Print(self):
        print("")
        print("Parent: " + str(self.parent.fitness) + " Child: " + str(self.child.fitness))
        print("")

    def Show_Best(self):
        # self.parent.Evaluate('GUI')
        pass