# Name: Dat , ID: 100886108

def main():
    file_object1 = open("inp_file.txt", mode= "w")
    file_object1.write("Python is an interpreted, high-level, and general-purpose programming language.")
    file_object1.close()

    Inputfile = input("Enter the input file name: ")
    Outputfile2 = input("Enter the output file name: ")

    print("\nDisplaying the contents of the input file.......\n")

    DisplayInputFile = open(Inputfile, mode="r")
    data = DisplayInputFile.read() 
    print(data)
    DisplayInputFile.close()

    
    try:
        DisplayOutputFile = open(Outputfile2, mode="r")
        DisplayOutputFile.close()
    except FileNotFoundError:
        print("\nout_file.txt does not exist!!\n")

    print("After copy from input to output")

    with open(Inputfile, mode="r") as f1, open(Outputfile2, mode="w") as f2:
        
        NumberOfCharacters = len(f1.read()) 
        NumberOfLines = len(f1.readlines())
        print("{} line and {} chars have been copied to output file".format(NumberOfLines, NumberOfCharacters))
        f2.write(f1.read())
        
        
"""    with open(Outputfile2, mode="a") as file_object2:
        file_object2.write("It was created by Guido van Rossum and first released in 1991.")

    print("After append to output file")

    with open(Outputfile2, mode="r") as file_object3:
        
        filedata = file_object3.read()
        UpdatedLines = len(file_object3.readlines())
        UpdatedNumofCharacters = len(file_object3.read())



    print("Updated count of lines in the output file is:", UpdatedLines)
    print("Updated count of characters in the output file is:", UpdatedNumofCharacters)
    print("\nDisplaying the contents of the output file....\n")
    print(filedata)"""

main()