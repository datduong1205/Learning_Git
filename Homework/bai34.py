# Hiển thị số đảo ngược của một số tự nhiên n nhập từ bàn phím (Không dùng xử lý chuỗi)

isParseDone = False

try:
    n = int(input("Type in 1 num: "))
    isParseDone = True
except ValueError:
    print("Invalid Error!")

if isParseDone:
    if n > 0:
        ReversedNum = 0
        while n > 0:
            LastNum = n % 10
            ReversedNum = ReversedNum * 10 + LastNum
            n = n // 10
        else:
            print("Reverse num is: {}".format(ReversedNum))
    elif n == 0:
        print("Result: {}".format(0))
    else: 
        print("n must be greater than or equal to 0")