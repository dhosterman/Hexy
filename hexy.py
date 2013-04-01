#To do: add debug flag for tracebacks

#sys configuration
import sys
sys.dont_write_bytecode = True  #don't clutter folders with .pyc files
sys.path.append("Moves")        #include the Moves folder
sys.path.append("PoMoCo")       #include the PoMoCo folder

#imports
import os, time, re, ConfigParser, servotorComm, traceback
from datetime import datetime
from robot import hexapod
from basic_moves import *
from memory import *
from communicate import *

#global variables
controller = servotorComm.Controller()      #servo controller
__builtins__.controller = controller
hexy = hexapod(controller)                  #Hexy!
__builtins__.hexy = hexy                    #sets hexy as global variable for all modules
__builtins__.floor = 60                     #minimum level the legs will reach
arguments = sys.argv                        #arguments passed to hexy on startup

def generateMoves():
    #create list of moves from Moves folder
    moves = ["Load Offsets"]
    for fileName in os.listdir("Moves"):
        if os.path.splitext(fileName)[1] == '.py':
            fileName = os.path.splitext(fileName)[0]
            s1 = re.sub('(.)([A-Z][a-z]+)', r'\1 \2', fileName)
            moves.append(s1)
    return moves
        
def move(moveName):
    #global function for running move files
    #print "Performing move:", moveName
    moveName = moveName.replace(" ","")
    if moveName in sys.modules:
        reload(sys.modules[moveName])
    else:
        __import__(moveName)

def loadOffsets():
    #if there is one offset file in the directory, automatically load it
    off_files = []
    for filename in os.listdir(os.getcwd()):
        start, ext = os.path.splitext(filename)
        if ext == ".cfg":
            off_files.append(filename)
    if len(off_files) == 1:
        print("I found %s, and am going to use it." % off_files[0])
        config = ConfigParser.ConfigParser()
        config.read(off_files[0])

        try:
            offsets = config.items("offsets")
            for offset in offsets:
                servoNum = int(offset[0])
                offset = int(offset[1])
                for servo in controller.servos:
                    if controller.servos[servo].servoNum == servoNum:
                        controller.servos[servo].setOffset(timing = offset)
                        break
            #print("Loaded offsets from %s" % off_files[0])
        except:
            print("I can't find my offsets. Did you misplace them?")
            
def getCommands(moves):
    #loop for request/process of moves
    memory = Interactions()                 #open interaction memory to record this time
    start_time = datetime.now()             #record the starting time of interaction for memory
    loop = True
    os.system("clear")
    print("Hexy: Hello.")
    while loop:
        time.sleep(1)                       #or the command prompt doesn't always appear
        user_input = Input(raw_input("Me: "))
        if user_input.isMove()[0] == True:
            try:
                move(user_input.read())
            except:
                print("Hexy: I'm afraid I can't do that right now.")
                #traceback.print_exc()
            move("Killall")
        elif user_input.inputParse() == True:
                loop = False
        else:
            print("Hexy: I don't understand what you want me to do.")
    memory.write([start_time, datetime.now(), 1])       #write interaction log to memory
            
if __name__ == "__main__":

    #these should always be done to initialize Hexy
    __builtins__.move = move            #make move a global variable for all modules
    moves = generateMoves()             #generate list of moves from the Moves folder
    loadOffsets()                       #load offsets and calibrate Hexy

    #this block performs moves that are entered as arguments from the command line activation of Hexy
    if len(arguments) > 1:              #perform argument list of commands
        for each in arguments[1:]:
            try:
                move(each.title())
                time.sleep(1)
            except:
                print("Hexy: I don't understand what you want me to do.")
                #traceback.print_exc()
                move("Killall")
                break

    #this block opens Hexy's interactive shell            
    else:
        getCommands(moves)              #loop to request and process commands
    
    del hexy
    del controller
    print("Hexy: Goodbye!")
    os._exit(0)
