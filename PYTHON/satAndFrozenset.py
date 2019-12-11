# sets. Sets are holding only unique elements in a random order.
f_set = {"John", "Alex", "Gragor", "Alex"} #creating and assigning a frozen set variable
print(f_set) # holds values without repeats.
s_set = set() # creating an empty frozen set
print(len(f_set)) # shoing amount of values in f_set
f_set.add("SomebodyElse") # adding an element into f_set
print(f_set)
# removing an element from frozen set
strVar = "SomebodyElse"
if strVar in f_set: # if an element exists,...
    f_set.remove(strVar) # removing it
print(f_set)

for value in f_set: #value is an variable
    print(value) # printing all values from f_set

print("Gragor" in f_set) # prints True, since element "Alex" exists in f_set
print("something" in f_set) # returnes False, since "something" doesn't exist in f_set
s_set = f_set.copy() # maks a copy from f_set into a s_set
print("s_set holds:", s_set) # s_set now is a separate independent copy of f_set

f_set.discard("not existed value") # if value doesn't exist, an error will not be throwen.
f_set.clear() # f_set is empty now, but still exists.
print(f_set) # f_set is empty, prints "set()"
print("is s_set holds anything:", s_set) # s_set still has all it's elements, since it's a separate independent copy of f_set

set1 = {"Pushkin", "Petrov", "Ivanov", "Sidorov"}
set2 = {"Pushkin", "Kazakov", "Petrushkin"}
set3 = set1.union(set2) # set3 now holds joined set1 and set2.
print(set3) # holds an all elements from both previous sets.
set3 = set1.intersection(set2) # set3 now holds only elements, that exists in both (set1 and set2) sets.
print(set3) # shows only "Pushkin", which exists in a both set1 and set2 sets.
set3 = set1.difference(set2) # shows only elements, that holds in both sets, but do not repeate in both.
print(set3) # shows all elements, but "Pushkin", since "Pushkin" exists in a both sets.
print(set1 - set2) # the same result as by the "difference" method.

big_set = {'Kazakov', 'Pushkin', 'Petrov', 'Sidorov', 'Petrushkin', 'Ivanov'}
print(set1.issubset(big_set)) # Returnes true, since big_set has at least all elements, which set1 has.
print(big_set.issuperset(set1)) # returnes true, because all elements from set1 are exist in a big_set


# Frozen Sets are holding unchangable and unremovable elements

frzs = frozenset({'Pushkin', 'Petrov', 'Sidorov', 'Petrushkin', 'Ivanov'}) #frozen set has been created
# there is not possible to add a new elements into a frozen sets.
