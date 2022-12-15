# Name: Dat , ID: 100886108

balance = float(0)
otherBalance = float(0) 

def getBalance():
    return balance

def getOtherBalance():
    return otherBalance

def printBalances():
    balance = "${:.2f}".format(getBalance())
    otherBalance = "${:.2f}".format(getOtherBalance())
    return balance, otherBalance

def deposit(money):
    if int(money) >= 0:
        global balance
        balance += money
        print("Money deposit successful!")
        return balance
    else:
        print("Invalid Input! Money entered should be greater than 0")

def withdraw(money):
    if money >= 0:
        global balance
        if money <= balance:
            balance -= money
            print("Money withdrawn successfully!")
            return balance
        else:
            print("Invalid Input! Money entered should be greater than 0 and less than or equal to balance")
    else:
        print("Invalid Input! Money entered should be greater than 0 and less than or equal to balance")

def transfer(money):
    if money >= 0:
        global balance, otherBalance
        if money <= balance:
            balance -= money
            otherBalance += money
            print("Money transfered successfully!")
            return balance, otherBalance
        else:
            print("Invalid Input! Money entered should be greater than 0 and less than or equal to balance")
    else:
        print("Invalid Input! Money entered should be greater than 0 and less than or equal to balance")

print("Welcome to the ATM machine!")

try:
    while True:
        UserEntered = int(input("Select:\n1: Balance\n2: OtherBalance\n3: Balance/OtherBalance\n4: Deposit\n5: Withdraw\n6: Transfer\n"))
        if UserEntered == 1:
            print(getBalance())
        elif UserEntered == 2:
            print(getOtherBalance())
        elif UserEntered == 3:
            print(*printBalances())
        elif UserEntered == 4 or UserEntered == 5 or UserEntered == 6:
            Money = int(input("Enter the amount of money: "))
            if UserEntered == 4:
                deposit(Money)
            elif UserEntered == 5:
                withdraw(Money)
            elif UserEntered == 6:
                transfer(Money)
        else:
            print("Invalid Input! ")
        
        NextExecute = input("Do you want to continue? (Y/N):")
        if NextExecute == "N":
            print("Exit")
            break
except ValueError:
    print("Invalid Input!")

