#Dicts: methods, ...
dct = {} # creating dict
dct2 = dict() # creating dict
print(type(dct)) # shoing type of variable dct
age = {"Peter":10, 1:155, "smth":"Something", "mm.":True, "Ivan":25, "igor":80}
print(age)
age["Feder"] = 3 # adding a new element to a DICT age
print(age) 
del age["Feder"] # Deliting the "Feder" element from dict age.
print(age)
print(age[1]) # shows 155 (element from key by name 1)
print(age.get(1)) # returnes value from key 1. the same result as age[1], but sometimes method get should be used
print(age["mm."]) # shows True (element from key by name "mm.")
print("smth" in age) # shows true, because the key "smth" exists in dict age.
age2 = age.copy()
print(age2) # age has been copied in to age2
age2.clear() # removing all from dict age2.
print(age2)
print(age.pop("smth")) # returnes "Something" (value from key "smth"), and the value with it's key "smth" will be delited
print(age) # the "smth" with it's value is no longer exists
print(age.popitem()) #returnes, and removes the last key and it's value from dict age
print(age) # the key last key 'igor' with it's value is no longer exists
print(list(age.keys())) # returnes all keys from dict age as a list
print(list(age.values())) # returnes all values from dict age as a list
dict1 = {"Petya": 1, "Dima":"admin", "Fedor":"Frodo"} #asiggning DICT
dict2 = {"Petya": 25, "Dima":"mentor", "Ivan":"Efremov"} #asiggning DICT
dict1.update(dict2) # updating dict1 by adding keys and values from dict2.
print(dict1)

for key in dict1: # shoing all keys and values in DICT dict1
    print(key,"--", dict1[key])

for key, value in dict1.items(): # shoing all keys and values in DICT dict1
    print(key, "---", value)

for key in dict1.keys(): # shoing all keys in DICT dict1
    print(key)

for value in dict1.values(): # shoing all values in DICT dict1
    print(value)












