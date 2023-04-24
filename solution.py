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
        if c.BRAIN_TYPE == "neural_network":
            self.weights = {}
            for botNum in range(numBots):
                SensorHidden = np.random.normal(c.mu, c.sigma, (c.numSensorNeurons, c.numHiddenNeurons))
                HiddenMotor = np.random.normal(c.mu, c.sigma, (c.numHiddenNeurons, c.numMotorNeurons))
                self.weights[botNum] = [SensorHidden, HiddenMotor]

        if c.BRAIN_TYPE == 'neural_network_recurrant':
            self.weights = {}
            for botNum in range(numBots):
                SensorHidden = np.random.normal(c.mu, c.sigma, (c.numSensorNeurons, c.numHiddenNeurons))
                HiddenMotor = np.random.normal(c.mu, c.sigma, (c.numHiddenNeurons, c.numMotorNeurons))
                HiddenHidden = np.random.normal(c.mu, c.sigma, (1, c.numHiddenNeurons))
                self.weights[botNum] = [SensorHidden, HiddenMotor, HiddenHidden]

        if c.BRAIN_TYPE == "hive_mind":

            # For each bot we will connect all sensors to the Hidden neurons
            # and the shared hidden neurons will each in turn attach to all of the motors
            # of each bot. So self.weights doesn't actually change much but instead breaking it
            # up by botNum we will send one massive array because of how generate_hive_mind
            # is currently set up

            SensorHidden = np.random.normal(c.mu, c.sigma, (c.numSensorNeurons * c.numBots, c.numHiddenNeurons))
            HiddenMotor = np.random.normal(c.mu, c.sigma, (c.numHiddenNeurons, c.numMotorNeurons * c.numBots))
            self.weights = [SensorHidden, HiddenMotor]

        if c.BRAIN_TYPE == "hive_mind_recurrant":
            SensorHidden = np.random.normal(c.mu, c.sigma, (c.numSensorNeurons * c.numBots, c.numHiddenNeurons))
            HiddenMotor = np.random.normal(c.mu, c.sigma, (c.numHiddenNeurons, c.numMotorNeurons * c.numBots))
            RecurrantHidden = np.random.normal(c.mu, c.sigma, (1, c.numHiddenNeurons))
            self.weights = [SensorHidden, HiddenMotor, RecurrantHidden]

        if c.BRAIN_TYPE == "hive_mind_recurrant_hybrid_A":
            # SensorHiddenHive
            SensorHiddenHive = np.random.normal(c.mu, c.sigma, (c.numSensorNeurons * c.numBots, int(c.numHiddenNeurons / 2)))

            # SensorHiddenLocal
            SensorHiddenLocal = np.random.normal(c.mu, c.sigma, (c.numSensorNeurons * c.numBots, int(c.numHiddenNeurons / 2)))

            # HiddenHiveMotors
            HiddenHiveMotor = np.random.normal(c.mu, c.sigma, (int(c.numHiddenNeurons / 2), c.numBots * c.numMotorNeurons))

            # HiddenLocalMotors
            HiddenLocalMotor = np.random.normal(c.mu, c.sigma, (int(c.numHiddenNeurons / 2), c.numBots * c.numMotorNeurons))

            # RecurrantHiddenHive
            RecurrantHidden = np.random.normal(c.mu, c.sigma, (1, int(c.numHiddenNeurons / 2)))

            # RecurrantHiddenLocal
            RecurrantLocal = np.random.normal(c.mu, c.sigma, (c.numBots, int(c.numHiddenNeurons / 2)))

            self.weights = [SensorHiddenHive, SensorHiddenLocal, HiddenHiveMotor, HiddenLocalMotor, RecurrantHidden, RecurrantLocal]


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

        fileRead = False
        while not fileRead:
            try:
                file = open("fitness" + str(self.myID) + ".txt", "r")
                fileRead = True
            except:
                time.sleep(0.1)

        self.fitness = float(file.read())
        file.close()
        os.system("del fitness" + str(self.myID) + ".txt")

    def Mutate(self):
        if c.BRAIN_TYPE == "neural_network":

            # Pick a random bot to update (as opposed to updating each one)
            botNum = random.randint(0, c.numBots - 1)

            ## Update synapse in Sensor -> Hidden OR Hidden -> Motor
            choice = random.randint(0, 1)

            if choice:
                randomRow = random.randint(0, c.numSensorNeurons - 1)
                randomColumn = random.randint(0, c.numHiddenNeurons - 1)
                self.weights[botNum][0][randomRow, randomColumn] = 2 * random.random() - 1
            else:
                randomRow = random.randint(0, c.numHiddenNeurons - 1)
                randomColumn = random.randint(0, c.numMotorNeurons - 1)
                self.weights[botNum][1][randomRow, randomColumn] = 2 * random.random() - 1

        if c.BRAIN_TYPE == 'neural_network_recurrant':

            # Pick a random bot to update (as opposed to updating each one)
            botNum = random.randint(0, c.numBots - 1)

            ## Update synapse in Sensor -> Hidden OR Hidden -> Motor
            choice = random.randint(0, 190)

            if choice >= 0 and choice < 60:
                randomRow = random.randint(0, c.numSensorNeurons - 1)
                randomColumn = random.randint(0, c.numHiddenNeurons - 1)
                self.weights[botNum][0][randomRow, randomColumn] = 2 * random.random() - 1
            elif choice >= 60 and choice < 180:
                randomRow = random.randint(0, c.numHiddenNeurons - 1)
                randomColumn = random.randint(0, c.numMotorNeurons - 1)
                self.weights[botNum][1][randomRow, randomColumn] = 2 * random.random() - 1
            else:
                randomColumn = random.randint(0, c.numHiddenNeurons - 1)
                self.weights[botNum][2][0, randomColumn] = 2 * random.random() - 1

        if c.BRAIN_TYPE == 'hive_mind':
            choice = random.randint(0, 1)

            if choice:
                randomRow = random.randint(0, c.numBots * c.numSensorNeurons - 1)
                randomColumn = random.randint(0, c.numHiddenNeurons - 1)
                self.weights[0][randomRow][randomColumn] = 2 * random.random() - 1
            else:
                randomRow = random.randint(0, c.numHiddenNeurons - 1)
                randomColumn = random.randint(0, c.numBots * c.numMotorNeurons - 1)
                self.weights[1][randomRow][randomColumn] = 2 * random.random() - 1

        if c.BRAIN_TYPE == 'hive_mind_recurrant':
            choice = random.randint(0, c.numBots*(180) + 10)

            if choice >= 0 and choice < (60 * c.numBots):
                randomRow = random.randint(0, c.numBots * c.numSensorNeurons - 1)
                randomColumn = random.randint(0, c.numHiddenNeurons - 1)
                self.weights[0][randomRow][randomColumn] = 2 * random.random() - 1
            elif choice >= (60 * c.numBots) and choice < (c.numBots * 180):
                randomRow = random.randint(0, c.numHiddenNeurons - 1)
                randomColumn = random.randint(0, c.numBots * c.numMotorNeurons - 1)
                self.weights[1][randomRow][randomColumn] = 2 * random.random() - 1
            else:
                randomColumn = random.randint(0, c.numHiddenNeurons - 1)
                self.weights[2][0][randomColumn] = 2 * random.random() - 1
        #TODO: change chance values here
        if c.BRAIN_TYPE == 'hive_mind_recurrant_hybrid_A':
            choice = random.randint(0, 6)

            if choice == 0:
                # Sensor HiddenHive
                randomRow = random.randint(0, c.numBots * c.numSensorNeurons - 1)
                randomColumn = random.randint(0, int(c.numHiddenNeurons / 2) - 1)
                self.weights[0][randomRow][randomColumn] = 2 * random.random() - 1

            elif choice == 1:
                randomRow = random.randint(0, c.numBots * c.numSensorNeurons - 1)
                randomColumn = random.randint(0, int(c.numHiddenNeurons / 2) - 1)
                self.weights[1][randomRow][randomColumn] = 2 * random.random() - 1

            elif choice == 2:
                randomRow = random.randint(0, int(c.numHiddenNeurons / 2) - 1)
                randomColumn = random.randint(0, c.numBots * c.numMotorNeurons - 1)
                self.weights[2][randomRow][randomColumn] = 2 * random.random() - 1

            elif choice == 3:
                randomRow = random.randint(0, int(c.numHiddenNeurons / 2) - 1)
                randomColumn = random.randint(0, c.numBots * c.numMotorNeurons - 1)
                self.weights[3][randomRow][randomColumn] = 2 * random.random() - 1

            elif choice == 4:
                randomColumn = random.randint(0, int(c.numHiddenNeurons / 2) - 1)
                self.weights[4][0][randomColumn] = 2 * random.random() - 1

            elif choice == 5:
                randomRow = random.randint(0, c.numBots - 1)
                randomColumn = random.randint(0, int(c.numHiddenNeurons / 2) - 1)
                self.weights[5][randomRow][randomColumn] = 2 * random.random() -1

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
        elif c.startPos == 'circle':
            for botNum in range(self.numBots):
                xCoord = c.startRadius * np.cos(2 * botNum * np.pi / c.numBots)
                yCoord = c.startRadius * np.sin(2 * botNum * np.pi / c.numBots)
                zCoord = 1
                startingIndex = generate.Generate_Body(self.bodyType, botNum, xCoord, yCoord, zCoord, startingIndex,
                                                       botNum)

    def Create_Brain(self):

        if c.BRAIN_TYPE == 'neural_network' or c.BRAIN_TYPE == 'neural_network_recurrant':
            for botNum in range(self.numBots):
                generate.Generate_Brain(self.myID, self.bodyType, botNum, self.weights[botNum])
        elif c.BRAIN_TYPE in {'hive_mind', 'hive_mind_recurrant', 'hive_mind_recurrant_hybrid_A',
                        'hive_mind_recurrant_hybrid_B'}:
            generate.Generate_Hive_Mind(self.myID, self.bodyType, self.weights)



    def Set_ID(self, newID):
        self.myID = newID