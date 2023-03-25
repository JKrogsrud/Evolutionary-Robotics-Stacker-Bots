import numpy as np
import constants as c
import pyrosim.pyrosim as pyrosim

class SENSOR:
    def __init__(self, linkName, botNum, numLinks):
        self.linkName = linkName
        self.botNum = botNum
        self.numLinks = numLinks
        # self.Prepare_To_Sense()

    def Prepare_To_Sense(self):
        self.values = np.zeros(c.SIM_LEN)

    def Get_Value(self):
        return pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName, self.botNum, self.numLinks)

    def Save_Values(self):
        np.save('data/' + self.linkName + 'SensorValues.npy', self.values)