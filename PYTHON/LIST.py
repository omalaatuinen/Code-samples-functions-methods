a = [1,2,3,10,"str","str 2"] # the list a is assigned
a[0] = 4 # a holds 4,2,3,10,"str","str 2"
b = a[:] # b is a copy of a (thу copy, not just the link to a)
b = list(a) # the same as before: b is a copy of a.
b = [10,15] # pyb holds 10,15
print(a) # shows [1,2,3,10,"str","str 2"]
c = a # c is linked to a (not a copy of a)
c.append(7) # 7 has been appended into the end of a. a holds [1,2,3,10,"str","str 2",7]
print(a) # shows [1,2,3,10,"str","str 2",7]
a.remove("str 2") # removes by value. removes first accured value. a holds [4,2,3,10,"str",7]
del a[4] #removes by index. a holds [4,2,3,10,7]
del a[-1] #removes by index from end. a holds [4,2,3,10]
b = [25,15] #assigning b,
b.extend(a) # b holds 25,15,1,2,3,10
print(a[1:3]) # shows values by indexes from 1 and up to (but not included) 3. a holds 2,3
a.insert(2,99) # a holds 4,2,99,3,10
print(a) # a holds 4, 2, 99, 3, 10
print(a.pop(2)) # removes value (99) by index from a, and return it's (previous) value: 2.
print(a) # a holds 4,2,3,10
print(a.index(10)) #returnes index of 10: 3.
a.append(4) # appending 4 in to the end of a
print(a.count(4)) # returnes count of values 4 in the list a.
a.sort() # sorts vslues to ascend.
print(a) # a holds 2, 3, 4, 4, 10
a.sort(reverse=True) # sorts vslues from larger to smaler.
print(a) # a holds 10, 4, 4, 3, 2

for i in a:
    print(i)# prints all values (elements) of a.

i = 0
while i < len(a):
    print(a[i])
    i += 1

a = [] # a holds nothing: []

# b = input()  possible to imput something into variable b

a = [i for i in range(5)] # a holds 0,1,2,3,4




