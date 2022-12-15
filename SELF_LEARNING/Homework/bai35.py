# Tính tích của tổng các chữ số chẵn và tổng các chữ số lẻ của một số tự nhiên nhập từ bàn phím.

isParseDone = False

try:
    n = int(input("Type in a num: "))
    isParseDone = True
except ValueError:
    print("Invalid Input!")

if isParseDone:
    if n > 0:
        SumEvenNum = 0
        SumOddNum = 0
        
        while n > 0:
            LastNum = n % 10
            if LastNum % 2 == 0:
                SumEvenNum += LastNum
            else:
                SumOddNum += LastNum
            n = n // 10
        else:
            Result = SumEvenNum * SumOddNum

        print("Result: {}".format(Result))
    else:
        print("n must be greater than 0")
