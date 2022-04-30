# Viết chương trình tính và hiển thị ra màn hình n giai thừa (n!). Với n là số tự nhiên nhập từ bàn phím.


isParseDone = False

try:
    n = int(input("Type in a num: "))
    isParseDone = True
except ValueError:
    print("Invalid Input!")

if isParseDone:
    if n >=  0:
        Factorial = 1
        for i in range(1, n+1):
            Factorial *= i
        print("Factorial of n: {} ".format(Factorial))
    else:
        print("num must be greater of equal 0")


