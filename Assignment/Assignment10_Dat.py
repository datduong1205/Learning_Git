# Name: Dat , ID: 100886108

def FindSum(mylist):
    result = []
    for i in mylist:
        SumOfNatural = (i*(i+1))/2
        result.append(SumOfNatural)
    return result

def PrintResult(mylist, resultlist):
    for i, j in enumerate(mylist):
        print(f'Sum of {mylist[i]} is: {resultlist[i]}')

def SaveResult(mylist, resultlist):
    with open('result.out', mode='w') as f1:
        for i, j in enumerate(mylist):
            f1.write(f'Sum of {mylist[i]} is: {resultlist[i]}\n')
    

numlist = []
while True:
    while True:
        try:
            UserInput = int(input('Please enter a positive number [enter -1 to stop]: '))
            if UserInput == -1:
                break
            elif UserInput > 0:
                numlist.append(UserInput)
        except ValueError:
            print('Invalid Input!')

    while True:
        try:
            Choice = int(input("Option:\n 1. Find Sum\n 2. Print Result\n 3. Save Result\n 4. Exit\n choose: "))
            if Choice == 1:
                result = FindSum(numlist)
                PrintResult(numlist, result)
                print()

            elif Choice == 2:
                PrintResult(numlist, result)
                print()

            elif Choice == 3:
                SaveResult(numlist, result)
                print('Save to the file.... Successfully!')
                print()

            elif Choice == 4:
                print('Exit!')
                print()
                break
        except ValueError:
            print("Invalid Input! Please enter from 1-4")

    NextAttempt = input("Do you want to continue ? [Y/N]: ").lower()
    if NextAttempt == 'n':
        print("Bye!")
        break


