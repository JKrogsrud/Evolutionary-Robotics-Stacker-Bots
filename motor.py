import pybullet as p

import constants as c
import pyrosim.pyrosim as pyrosim
import numpy as np
import generate
class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.Prepare_To_Act()

    def Prepare_To_Act(self):

        self.motorValues = generate.Generate_Oscillation(c.bodytype, self.jointName)

        # self.amplitude = c.FRONT_AMP
        # self.frequency = c.FRONT_FREQ
        # self.offset = c.FRONT_PHASE
        #
        # if self.jointName == "Torso_BackLeg":
        #     self.frequency = c.FRONT_FREQ / 2
        #
        # x = np.linspace(start=0 - self.offset, stop=2 * np.pi - self.offset, num=c.FRAMES) * self.frequency
        # self.motorValues = np.sin(x)*self.amplitude


    def Set_Value(self, robotID, time_stamp):

        pyrosim.Set_Motor_For_Joint(bodyIndex=robotID,
                                    jointName=self.jointName,
                                    controlMode=p.POSITION_CONTROL,
                                    targetPosition=self.motorValues[time_stamp % c.FRAMES],
                                    maxForce=c.MAX_FORCE)

    # THE FOLLOWING IS FOR A TRUE NN FOR OSCILLATORY MOVEMENT WE WILL USE A DIFFERENT FUNCTION
    # def Set_Value(self, robotID, desiredAngle):
    #
    #     pyrosim.Set_Motor_For_Joint(bodyIndex=robotID,
    #                                 jointName=self.jointName,
    #                                 controlMode=p.POSITION_CONTROL,
    #                                 targetPosition=desiredAngle,
    #                                 maxForce=c.MAX_FORCE)

    # def Save_Values(self):
    #     np.save('data/' + self.jointName + 'MotorValues.npy', self.motorValues)