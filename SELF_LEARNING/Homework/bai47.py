# Viết hàm hiển thị tích của tổng chữ số chẵn và tổng chữ số lẻ của một số tự nhiên

def Sum(n):
    if n > 0:
        EvenNum = 0
        OddNum = 0
        while n > 0:
            LastNum = n % 10
            if LastNum % 2 == 0:
                EvenNum += LastNum
            else:
                OddNum += LastNum          
            n = n // 10
        else:
            return EvenNum * OddNum
    else:
        print("n must be greater than 0")

isParseDone = False

try:  
    n = int(input("Type in 1 num: "))      
    isParseDone = True
except ValueError:
    print("Invalid Input!")

if isParseDone:
    print(Sum(n))
