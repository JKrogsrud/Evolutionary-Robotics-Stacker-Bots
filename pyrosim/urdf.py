class URDF:

    def __init__(self):

        self.depth = 0

    def Save_Start_Tag(self, f, botName):

        f.write('<robot name = "robot' + str(botName) + '">\n')

    def Save_End_Tag(self, f):

        f.write("</robot>")
