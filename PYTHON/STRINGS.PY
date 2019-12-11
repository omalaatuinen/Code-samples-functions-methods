# strings
s = "Hello world" # "" and '' are the same
print(s[1])

for i in s:
    print(i)
print(s[:4]) # shows first 4 symbols
print(s[3:9]) # shos from 4 till 9 symbols
print(s[3:]) # prints from symbol 4 till the end of string s
print(len(s))# returnes string's length.
if "Hello" in s: # searching in string s
    print('"Hello" exists in s.')
if "hello" in s:# nothing will be printed.
    print("there is no hello in str. s.")
print("hello" in s) #returnes false.
print(s.upper())# returnes HELLO WORLD
print(s.lower()) # returnes hello world
lst = s.split()# lst now is LIST of two words: ['Hello', 'World']
print(lst) 
s2 = ' '.join(lst) # returnes "Hello world"
print(s2)
s2 = '---'.join(lst) # returnes "Hello---world"
print(s2)
print(s.find("world")) # returnes a first index, from which 'world' begins: 6
print(s.find("abra_cadabra")) # returnes -1 as a falue.
print(s.replace("world", "Alex")) # prints "Hello Alex".
s2 = "length - {}, height - {}, width - {}"
print(s2.format(5,6,7)) # prints length - 5, height - 6, width - 7
s = "Hello, {name}" # name will be used as a parameter for .format()
print(s.format(name="John")) # returnes Hello John
print(dir(s)) # shows all available methods for string s