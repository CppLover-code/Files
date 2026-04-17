print("Working with files")

#with open("ReadFile.txt", "r") as readFile:
    #print("Working with a file ReadFile.txt")

try:
    readFile = open("ReadFile.txt", "r")
    try:
        print("Working with a file ReadFile.txt")
        for line in readFile:
            print(line, end="")
    finally:
        readFile.close()
except Exception as ex:
    print("Error", ex)
