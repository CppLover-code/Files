print("Working with files")

"""
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
"""

"""
try:
    with open("ReadFile.txt", "r") as readFile:
        print("Reading a file ReadFile.txt")
        for line in readFile:
            print(line, end="")
except FileNotFoundError as ex:
    print("Error", ex)

try:
    with open("WriteFile.txt", "w") as writeFile:
        print("Writing a file WriteFile.txt")
        writeFile.write("hello world")
        print("File written successfully!")
except FileNotFoundError as ex:
    print("Error", ex)

try:
    with open("WriteFile.txt", "a") as writeFile:
        print("Writing a file WriteFile.txt")
        writeFile.write("\nhello work")
        print("File modified successfully!")
except FileNotFoundError as ex:
    print("Error", ex)
"""

fileName = "testFile.txt"

def write():
    message = input("Enter the string: ")
    with open(fileName,"w") as file:
        file.write(message + "\n")

def read():
    try:
        with open(fileName, "r") as file:
            for text in file:
                print(text, end = "")
        print()
    except FileNotFoundError as ex:
        print("Attention: ", ex)

while(True):
    selection = int(input("1. Write to file\t\t2. Reading a file\t\t3. Exit\nSelect action: "))
    match selection:
        case 1: write()
        case 2: read()
        case 3: break
        case _: print("Invalid input!")

print("The program is completed!")


