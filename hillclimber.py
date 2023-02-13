from solution import SOLUTION
from constants import *
import copy as cp
class HILLCLIMBER:

    def __init__(self):
        self.parent = SOLUTION()
        pass

    def Evolve(self):
        self.parent.Evaluate()
        for currentGeneration in range(numberOfGenerations):
            self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate()
        self.Print()
        self.Select()


    def Spawn(self):
        self.child = cp.deepcopy(self.parent)

    def Mutate(self):
        self.child.Mutate()

    def Select(self):
        if self.parent.fitness > self.child.fitness:
            self.parent = self.child

    def Print(self):
        print("Parent: " + str(self.parent.fitness))
        print("Child: " + str(self.child.fitness))
