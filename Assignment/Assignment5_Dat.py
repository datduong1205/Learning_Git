# Name: Dat , ID: 100886108

def CheckEvenOdd(mylist):
    EvenList = [x for x in mylist if x % 2 == 0]
    OddList = [x for x in mylist if x % 2 == 1]
    return EvenList, OddList

def CalculateAverage(mylist):
    Evenlist, Oddlist = CheckEvenOdd(mylist)
    AverageEven = 0
    AverageOdd = 0
    for i in Evenlist:
        AverageEven += i
    for i in Oddlist:
        AverageOdd += i
    
    Average = AverageEven + AverageOdd
    return AverageEven, AverageOdd, Average

def PrintResult(AverageEven, AverageOdd, Average):
    print("Even total:", AverageEven)
    print("Odd total:", AverageOdd)
    print("Total:", Average)

def CalculatePow(mylist):
    PowList = []
    for i in mylist:
        IndexNum = mylist.index(i)
        Result = pow(i, IndexNum)
        PowList.append(Result)
    return PowList


listnum = []

while True:
    while True:
        num = int(input("Please enter random number: "))
        if num == -1:
            break
        else:
            listnum.append(num)

    Evenlist, Oddlist = CheckEvenOdd(listnum)
    AverageEven, AverageOdd, Average = CalculateAverage(listnum)

    PrintResult(AverageEven, AverageOdd, Average)

    print(*CalculatePow(listnum))




