# Viết hàm trả về tổng các số từ 1 đến n (Dùng đệ quy). Với tham số là số tự nhiên n.

isParseDone = False

def Sum(n):
    if n == 0:
        return 0
    else:
        return n + Sum(n-1)

try:
    n = int(input("Type in 1 num: "))
    isParseDone = True
except ValueError:
    print("Invalid Input!")

if isParseDone:
    if n < 0:
        print("n must be greater than 0")
    else:
        print("sum: {}".format(Sum(n)))
