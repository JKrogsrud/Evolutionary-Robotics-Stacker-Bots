import pybullet as p
import constants as c
import pyrosim.pyrosim as pyrosim
import generate
import numpy as np


class MOTOR:
    def __init__(self, jointName, numBots):
        self.jointName = jointName
        self.numBots = numBots
        self.Prepare_To_Act()
        self.value = 0


    def Prepare_To_Act(self):
        self.values = np.zeros(c.SIM_LEN)

        if c.BRAIN_TYPE == 'oscillatory':
            self.motorValues = generate.Generate_Oscillation(c.bodytype, self.jointName, self.numBots)
        elif c.BRAIN_TYPE == 'ragdoll':
            pass
        elif c.BRAIN_TYPE == 'rigid':
            pass
        elif c.BRAIN_TYPE == 'neural_network':
            pass
        elif c.BRAIN_TYPE == 'hive_mind':
            pass

    def Set_Value(self, robotID, time_stamp):

        if c.BRAIN_TYPE == 'oscillatory':
            pyrosim.Set_Motor_For_Joint(bodyIndex=robotID,
                                        jointName=self.jointName,
                                        controlMode=p.POSITION_CONTROL,
                                        targetPosition=self.motorValues[time_stamp % c.FRAMES],
                                        maxForce=c.MAX_FORCE)
        if c.BRAIN_TYPE == 'rigid':
            pyrosim.Set_Motor_For_Joint(bodyIndex=robotID,
                                        jointName=self.jointName,
                                        controlMode=p.POSITION_CONTROL,
                                        targetPosition=generate.Generate_Rigidity(c.bodytype, self.jointName, self.numBots),
                                        maxForce=c.MAX_FORCE)

    def Set_Value_NN(self, robotID, desiredAngle):
        self.value = desiredAngle
        pyrosim.Set_Motor_For_Joint(bodyIndex=robotID,
                                    jointName=self.jointName,
                                    controlMode=p.POSITION_CONTROL,
                                    targetPosition=desiredAngle,
                                    maxForce=c.MAX_FORCE)

    def Record_Value(self, t):
        self.values[t] = self.value


    # def Save_Values(self):
    #     np.save('data/' + self.jointName + 'MotorValues.npy', self.motorValues)