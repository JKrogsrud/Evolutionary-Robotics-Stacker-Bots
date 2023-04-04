from pyrosim.commonFunctions import Save_Whitespace

class MATERIAL: 

    def __init__(self, color):

        self.depth  = 3

        self.string1 = '<material name="' + str(color[0]) + '">'

        self.string2 = '    <color rgba='
        self.string3 = '"' + str(color[1]) + ' ' \
                       + str(color[2]) + ' ' \
                       + str(color[3]) + ' ' \
                       + str(color[4]) + '"'
        self.string4 = '/>'

        self.string5 = '</material>'

    def Save(self,f):

        Save_Whitespace(self.depth,f)

        f.write( self.string1 + '\n' )

        Save_Whitespace(self.depth,f)

        f.write( self.string2 + '\n' )

        Save_Whitespace(self.depth,f)

        f.write( self.string3 + '\n' )

        Save_Whitespace(self.depth, f)

        f.write(self.string4 + '\n')

        Save_Whitespace(self.depth, f)

        f.write(self.string5 + '\n')
