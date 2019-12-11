# this file will be loaded, and executed in another .py file.

def myNewFunc(x,y): # declaring a function
    return int(x) + int(y)
# if this file will be runing separatelly (as a main program), we can detect that, and perform some actions:
if __name__=="__main__": # if separatelly (as main program)
    print("This module has been runned separatelly") #throwing message about that
    print(myNewFunc("2","2")) # and do something else
else:
    print("Module has been suсcessfully imported") #such message appears emmidiatelly as module be loaded.
