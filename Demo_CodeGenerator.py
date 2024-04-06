#conding=utf-8

from FileHandler import WritetoFile
import sys

PwdPath = sys.argv[0]

class BuildCode_Dev:
    'Auto Generate code of Device control'

    def __init__(self, KeyWord = 'TestDemoCommand'):
        self.CmdKeyWord = KeyWord

    def Generate(self):
        fileName = 'Code_Dev.txt'

        mycode = []  
		#想生成什么样的代码就在mycode中append相应的行，
        mycode.append('\n---------------------- Demo code Below: ---------------------- ')

        mycode.append('\n---------------------- Demo code Below: ---------------------- ')  

        mycode.append('\n---------------------- Demo code Below: ---------------------- ')
        mycode.append('\n***** DemoCode_Get_DataLength() *****  ')
        mycode.append('\n***** DemoCode_Set_DataLength() *****  ')

        mycode.append('Switch ('+ self.CmdKeyWord + '):')
        mycode.append('    case('+ self.CmdKeyWord + '):') 
        mycode.append('    break;') 


        WritetoFile(fileName,mycode)

        print('Code:'+self.CmdKeyWord + ' Generator OK!')

        return(mycode)



if __name__ == '__main__':
    if(sys.argv[1:] == []):
        print('Not input parameter , Use Test Data')
        CmdKeyWord = 'TestDemoCommand'
    else:
        CmdKeyWord = sys.argv[1]
        
    
#code = BuildCode_Dev(CmdKeyWord)
#code.Generate()


#print(PwdPath)
#print(CmdKeyWord)