import random

import numpy as np
import pyrosim.pyrosim as pyrosim
import os
import time

import constants as c
import generate
from simulation import SIMULATION

class SOLUTION:
    def __init__(self, nextAvailableID, bodyType, numBots):
        # print("Here I am in SOLUTION with: " + str(nextAvailableID) + str(bodyType) + str(numBots))
        self.myID = nextAvailableID
        self.bodyType = bodyType
        self.numBots = numBots
        # Enable weights here for easy modification in Mutate call
        self.weights = {}
        if c.MOTION_TYPE == "neural_network":
            for botNum in range(numBots):
                SensorHidden = 2*np.random.rand(c.numSensorNeurons, c.numHiddenNeurons)-1
                HiddenMotor = 2*np.random.rand(c.numHiddenNeurons, c.numMotorNeurons)-1
                self.weights[botNum] = [SensorHidden, HiddenMotor]

    def Start_Simulation(self, DirectOrGUI):

        # print("Creating Worlds:")
        self.Create_World()
        # print("Creating Bodies:")
        self.Create_Body()
        # print("Creating Brains:")
        self.Create_Brain()

        os.system('START /B "" "C:\\Users\\Jared Krogsrud\\AppData\\Local\\Programs\\Python\\Python310\\python.exe" simulate.py ' + DirectOrGUI + ' ' + str(self.myID) + ' ' + self.bodyType + ' ' + str(self.numBots))

        # os.system('START "a" /B "C:\\Users\\Jared Krogsrud\\AppData\\Local\\Programs\\Python\\Python310\\python.exe" '
        #           'simulate.py ' + str(DirectOrGUI) + ' ' + str(self.myID) + ' ' + str(self.bodyType) + ' ' + str(self.numBots))

        # os.system('START /B "C:\\Users\\Jared Krogsrud\\AppData\\Local\\Programs\\Python\\Python310\\python.exe" simulate.py 4 GUI 0 A 3')

        # os.system('START /B "" "C:\\Users\\Jared Krogsrud\\AppData\\Local\\Programs\\Python\\Python310\\python.exe" '
        #           'simulate.py' + ' ' + DirectOrGUI + ' ' + str(self.myID))

        # os.system('START /B "" "C:\\Users\\Jared Krogsrud\\AppData\\Local\\Programs\\Python\\Python310\\python.exe" simulate.py')

        # Running Simulation:

        # sim = SIMULATION(DirectOrGUI, self.myID, self.bodyType, self.numBots)
        # sim.run()

    def Wait_For_Simulation_To_End(self):

        while not os.path.exists("fitness" + str(self.myID) + ".txt"):
            time.sleep(0.01)

        file = open("fitness" + str(self.myID) + ".txt", "r")
        self.fitness = float(file.read())
        file.close()
        os.system("del fitness" + str(self.myID) + ".txt")

    def Mutate(self):
        for botNum in range(self.numBots):
            ## Update synapse in Sensor -> Hidden OR Hidden -> Motor
            choice = random.randint(0, 1)

            randomRow = random.randint(0, c.numSensorNeurons - 1)
            randomColumn = random.randint(0, c.numHiddenNeurons - 1)
            #TODO: Finish up working one synapses
            if choice:
                self.weights[botNum][0] =

            randomRow = random.randint(0, c.numSensorNeurons - 1)
            randomColumn = random.randint(0, c.numMotorNeurons - 1)
            self.weights[botNum][randomRow, randomColumn] = 2 * random.random() - 1


    def Create_World(self):
        pyrosim.Start_SDF("world.sdf", 0)  # Creates file where world info will be stored

        pyrosim.End()  # Close sdf file

    def Create_Body(self):

        startingIndex = -1
        if c.startPos == 'horizontal':
            for botNum in range(self.numBots):
                xCoord = 0 + botNum * c.botSpacing
                yCoord = 0
                zCoord = 1
                startingIndex = generate.Generate_Body(self.bodyType, botNum, xCoord, yCoord, zCoord, startingIndex, botNum)
                # print(startingIndex)
        elif c.startPos == 'stacked':
            for botNum in range(self.numBots):
                xCoord = 0
                yCoord = 0
                zCoord = 0.5 + botNum * c.botSpacing
                startingIndex = generate.Generate_Body(self.bodyType, botNum, xCoord, yCoord, zCoord, startingIndex, botNum)

    def Create_Brain(self):

        for botNum in range(self.numBots):
            generate.Generate_Brain(self.myID, self.bodyType, botNum, self.weights[botNum][0], self.weights[botNum][1])


    def Set_ID(self, newID):
        self.myID = newID