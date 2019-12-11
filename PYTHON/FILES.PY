file = open("ex.txt", "a") #open file for append
file.write("Test of writing into txt file.\n") # \n used to add a new row.
file.close()

with open("ex.txt", "r") as f: # opening file like this, we do not have to close it.
    print(f.read(5)) #reading first 5 symbols from file. Next "open" command will continue reading from previous place.
    print(f.read()) #reading all file
    for line in f:
        print(line)
    print(f.readline()) #reading file's line

with open("ex.txt","a") as file:
    print("finish string\n", file=file)# the "finish string\n" will be added into file
