import pybullet as p

from pyrosim.nndf import NNDF

from pyrosim.linksdf  import LINK_SDF

from pyrosim.linkurdf import LINK_URDF

from pyrosim.model import MODEL

from pyrosim.sdf   import SDF

from pyrosim.urdf  import URDF

from pyrosim.joint import JOINT

SDF_FILETYPE  = 0

URDF_FILETYPE = 1

NNDF_FILETYPE   = 2

global availableLinkIndex

global linkNamesToIndices

def End():
    global availableLinkIndex

    if filetype == SDF_FILETYPE:

        sdf.Save_End_Tag(f)

    elif filetype == NNDF_FILETYPE:

        nndf.Save_End_Tag(f)
    else:
        urdf.Save_End_Tag(f)

    f.close()
    return availableLinkIndex

def End_Model():

    model.Save_End_Tag(f)


def Get_Touch_Sensor_Value_For_Link(linkName, botNum, numLinks):
    touchValue = -1.0

    # print("Get_Touch_Sensor_Value_For_Link: " + str(linkName) + " Bot: " + str(botNum))

    # Check using dict (desired number of values)
    desiredLinkIndex = linkNamesToIndices[linkName]
    print(linkNamesToIndices)
    # print("Desired Link Index:" + str(desiredLinkIndex))

    # This right here is what reports the sensors which are getting set wrong
    # print(botNum)
    pts = p.getContactPoints(botNum)
    # print(pts)
    for pt in pts:

        linkIndex = pt[4] + (botNum - 1) * numLinks
        # print("Link Index found by pybullet:")
        # print(linkIndex)
        # print("Bot: " + str(botNum) + " Link Index: " + str(linkIndex) + " desired Link Index: " + str(desiredLinkIndex))
        if (linkIndex == desiredLinkIndex):

            touchValue = 1.0

    return touchValue


def Prepare_Link_Dictionary(bodyIDList):

    global linkNamesToIndices

    linkNamesToIndices = {}

    linkInfoDict = {}
    linkIndexOffset = 0
    for bodyID in bodyIDList:
        linkNames = []
        # for jointIndex in range(0 + linkIndexOffset, p.getNumJoints(bodyID) + linkIndexOffset):
        for jointIndex in range(0, p.getNumJoints(bodyID)):
            # print(bodyID, jointIndex)
            jointInfo = p.getJointInfo(bodyID, jointIndex)
            # print(jointInfo)
            jointName = jointInfo[1]

            jointName = jointName.decode("utf-8")

            jointName = jointName.split("_")

            linkName = jointName[1]

            linkNames.append(linkName)

            linkNamesToIndices[linkName] = jointIndex + linkIndexOffset

            if jointIndex == 0:

                rootLinkName = jointName[0]

                linkNamesToIndices[rootLinkName] = -1

        linkInfoDict[bodyID] = linkNames
        linkIndexOffset += p.getNumJoints(bodyID)
    return linkInfoDict


def Prepare_Joint_Dictionary(bodyIDList):

    global jointNamesToIndices

    jointNamesToIndices = {}

    jointInfoDict = {}

    jointIndexOffset = 0

    # print("Prepare_Joint_Dictionary")
    for bodyID in bodyIDList:
        jointNames = []
        # for jointIndex in range(0+ jointIndexOffset, p.getNumJoints(bodyID)+jointIndexOffset):
        for jointIndex in range(0, p.getNumJoints(bodyID)):

            jointInfo = p.getJointInfo(bodyID, jointIndex)

            jointName = jointInfo[1].decode('UTF-8')
            # print(jointName)
            jointNames.append(jointName)

            jointNamesToIndices[jointName] = jointIndex + jointIndexOffset


        jointIndexOffset += p.getNumJoints(bodyID)
        jointInfoDict[bodyID] = jointNames
        jointInfoDict["numJoints"] = p.getNumJoints(bodyID)
    return jointInfoDict

def Prepare_To_Simulate(bodyIDList):

    linkInfo = Prepare_Link_Dictionary(bodyIDList)

    jointInfo = Prepare_Joint_Dictionary(bodyIDList)

    print(linkInfo)
    print(jointInfo)
    print(linkNamesToIndices)

    return linkInfo, jointInfo

def Send_Cube(name="default", pos=[0, 0, 0], size=[1, 1, 1]):

    global availableLinkIndex
    # print("In Send_Cube: linkIndex:" + str(availableLinkIndex))

    global links

    if filetype == SDF_FILETYPE:

        Start_Model(name, pos)

        link = LINK_SDF(name, pos, size)

        links.append(link)
    else:
        link = LINK_URDF(name, pos, size)

        links.append(link)

    link.Save(f)

    if filetype == SDF_FILETYPE:

        End_Model()

    linkNamesToIndices[name] = availableLinkIndex

    availableLinkIndex = availableLinkIndex + 1


def Send_Joint(name, parent, child, type, position, jointAxis):

    joint = JOINT(name, parent, child, type, position)

    joint.Save(f, jointAxis)


def Send_Motor_Neuron(name,jointName):

    f.write('    <neuron name = "' + str(name) + '" type = "motor"  jointName = "' + jointName + '" />\n')


def Send_Sensor_Neuron(name,linkName):

    f.write('    <neuron name = "' + str(name) + '" type = "sensor" linkName = "' + linkName + '" />\n')


def Send_Synapse( sourceNeuronName , targetNeuronName , weight ):

    f.write('    <synapse sourceNeuronName = "' + str(sourceNeuronName) + '" targetNeuronName = "' + str(targetNeuronName) + '" weight = "' + str(weight) + '" />\n')

 
def Set_Motor_For_Joint(bodyIndex,jointName,controlMode,targetPosition,maxForce):

    p.setJointMotorControl2(

        bodyIndex      = bodyIndex,

        jointIndex     = jointNamesToIndices[jointName],

        controlMode    = controlMode,

        targetPosition = targetPosition,

        force          = maxForce)

def Start_NeuralNetwork(filename):

    global filetype

    filetype = NNDF_FILETYPE

    global f

    f = open(filename, "w")

    global nndf

    nndf = NNDF()

    nndf.Save_Start_Tag(f)

def Start_SDF(filename, currentIndex):

    global availableLinkIndex

    availableLinkIndex = currentIndex

    global linkNamesToIndices

    linkNamesToIndices = {}

    global filetype

    filetype = SDF_FILETYPE

    global f
 
    f = open(filename, "w")

    global sdf

    sdf = SDF()

    sdf.Save_Start_Tag(f)

    global links

    links = []

def Start_URDF(filename, currentIndex, botName):

    global availableLinkIndex

    availableLinkIndex = currentIndex

    global linkNamesToIndices

    linkNamesToIndices = {}

    global filetype

    filetype = URDF_FILETYPE

    global f

    f = open(filename,"w")

    global urdf 

    urdf = URDF()

    urdf.Save_Start_Tag(f, botName)

    global links

    links = []

def Start_Model(modelName,pos):

    global model 

    model = MODEL(modelName,pos)

    model.Save_Start_Tag(f)
