a = "something" # string
a2 = a # assigning
b =[1,3,2,6,5] # List.
c =(1,3,2,6,5) # Tuple.
c2 =tuple([1,3,2,6,5]) # Tuple.
lst = [1,2,3] # List lst
tpl = tuple(lst) # now lst is assignet to tpl, and tpl has type tuple
print(type(tpl))
print(len(tpl)) #shows how many elements tuple tpl holds, shows 3

print(b.__sizeof__()) # shows size of list b
print(c.__sizeof__()) # shows size of Tuple c
print(c2.__sizeof__()) # shows size of Tuple c2
print(type(c2)) #shows variable type: <class tuple>
print(c[0]) #shows element 1, which is by index 0
print(c[-1]) #shows the last element (by the last index), shows 5

print(c[1:3]) #shows elements from index 1, till (but not included) index 3.
c = () #c now is empty
del a # now a is not defined (not exists)
print(c) #shows empty c

user = ("Alex", 27, True)
uName, uAge, isAdmin = user # uName holds "Alex", uAge holds 27, isAdmin holds True

def func():
    return 15,10,18 #function returnes 3 variables.
tpl = func() # TUPLE tpl gets 3 variable at once from function func
print(tpl)

for i in tpl: # itirating through all tpl elements
    print(i)
i = 0
while i < len(tpl):
    print(tpl[i]) #itirating through all tpl elements
    i += 1

if 18 in tpl: #looking for 18 in TUPLE tpl
    print("tpl has an element ", 18)
else:
    print("There is no element", 18, "in TUPLE tpl.")
