import pybullet as p
import constants as c
import pyrosim.pyrosim as pyrosim
import generate


class MOTOR:
    def __init__(self, jointName, numBots):
        self.jointName = jointName
        self.numBots = numBots
        self.Prepare_To_Act()


    def Prepare_To_Act(self):

        if c.MOTION_TYPE == 'oscillatory':
            self.motorValues = generate.Generate_Oscillation(c.bodytype, self.jointName, self.numBots)
        elif c.MOTION_TYPE == 'ragdoll':
            pass
        elif c.MOTION_TYPE == 'rigid':
            #TODO: Working on rigid body
            pass

    def Set_Value(self, robotID, time_stamp):

        if c.MOTION_TYPE == 'oscillatory':
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