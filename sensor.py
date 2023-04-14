import numpy as np
import constants as c
import pyrosim.pyrosim as pyrosim

class SENSOR:
    def __init__(self, linkName, botNum):
        self.linkName = linkName
        self.botNum = botNum
        self.Prepare_To_Sense()

    # This is used for data acquisition
    def Prepare_To_Sense(self):
        self.values = np.zeros(c.SIM_LEN)

    def Record_Value(self, t):
        if t >= c.SIM_LEN:
            pass
        else:
            self.values[t] = self.Get_Value()

    def Get_Value(self):
        return pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName, self.botNum)

    def Save_Values(self):
        np.save('data/' + self.linkName + 'SensorValues.npy', self.values)