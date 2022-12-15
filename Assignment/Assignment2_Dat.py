# Name: Dat , ID: 100886108

def CheckStatus(a):
    if a == "Exit" or a == "Stop":
        print("Process finished with exit code 0")
        return True
    return False

print("Welcome to the calculator")

try:
    while True:
        operator = input("Select operations to perform (add(+), subtract(-), multiply(*), divide(/), exponential(**) or Exit/Stop): ")
        if CheckStatus(operator):
            break
        num1 = input("Type in first num: ")
        if CheckStatus(num1):
            break
        num2 = input("Type in second num: ")
        if CheckStatus(num2):
            break

        if num1 == "":
            num1 = PreviousNum
        if num2 == "":
            num2 = PreviousNum
        
        num1, num2 = map(float, (num1, num2))
        if operator == "add" or operator == "+":
            Result = num1 + num2
            print("{} + {} = {}".format(num1, num2, Result))

        elif operator == "subtract" or operator == "-":
            Result = num1 - num2
            print("{} - {} = {}".format(num1, num2, Result))

        elif operator == "multiply" or operator == "*":
            Result = num1 * num2
            print("{} * {} = {}".format(num1, num2, Result))

        elif operator == "divide" or operator == "/":
            Result = num1 / num2
            print("{} / {} = {}".format(num1, num2, Result))

        elif operator == "exponential" or operator == "**":
            Result = 1
            for i in range(int(num2)):
                Result *= num1
            print("{} ** {} = {}".format(num1, num2, Result))

        NextCalculation = input("Do you want to continue? Type Y/N: ")
        if NextCalculation == "N":
            break
        PreviousNum = Result
        
except ValueError:
    print("Invalid Input!")
except ZeroDivisionError:
    print("Cannot be divided by zero!")