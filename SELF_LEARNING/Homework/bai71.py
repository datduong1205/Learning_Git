# Viết hàm trả về list số tự nhiên và list bình phương các số tự nhiên nhỏ hơn n (Với n là tham số tự nhiên)

def num_SquareNume(n):
    NumList = [i for i in range(n)]
    SquareNumList = [i*i for i in range(n)]
    return NumList, SquareNumList

try:
    n = int(input("Type in a num: "))
    if n < 0:
        print("{} must be greater than 0".format(n))
    else:
        NumList, SquareNumList = num_SquareNume(n)
        print(*NumList)
        print(*SquareNumList)
except ValueError:
    print("Invalid Input!")