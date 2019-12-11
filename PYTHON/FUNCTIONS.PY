def someFunc(x,y=10): # y has a defoult value 10 (if nothing will be given)
    return x*y
print(someFunc(2,3)) # shows 6
print(someFunc(3)) # shows 30

def strCon(name):
    print("Hello, "+name) #shows 'Hello, pupkin V.'. Concatination works with both "+" and ","
    print("Hello, ", name) #shows 'Hello, pupkin V.'
strCon("pupkin V.") #calling function

def factCalc(n): #calculating factorial with a cycle for.
    prod = 1
    for i in range(1, n+1):
        prod *= i
    return prod
print(factCalc(5)) #shows 120 (factorial of 5)
import math #importing math object of functions (methods)
f = math.factorial #function math.factorial is assigned now to f variable
print(f(4)) #shows 24 (factorial of 4)

sqr = lambda x: x ** 0.5
print(int(sqr(36))) # shows 6.

l = [5,4,3,6,2,1] #list l.
print(list(map(lambda x: x ** 3, l))) #increasing each l's element in power of 3
