# other module (.py) files can be loaded into another file. For example, into this one.
import math, datetime # a standard "math" and "datetime" modules have been loaded
print(math.factorial(4)) # shows factorial of number 4
print(datetime.datetime.now()) #shows a current date in a full format
import ex_module # our module has been loaded
print(ex_module.myNewFunc(3,"2")) #calling a function myNewFunc from a ex_module.py
import ex_module as m # now we can call functions as m.myNewFunc()
print(m.myNewFunc("10",2)) # now, code is a bit shorter.
from ex_module import myNewFunc # now, myNewFunc has been imported from another file, and can be directly called.
print(myNewFunc(5,5)) # we've called myNewFunc without module name.
from ex_module import * # now, all functions from file (module) ex_module.py have been imported, and can be directly called.
