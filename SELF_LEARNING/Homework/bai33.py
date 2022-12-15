# Viết chương trình tính và hiển thị ra màn hình kết quả của biểu thức sau: S(n) = 1 - x + x^2/2! - x^3/3! + … - x^(2n-1)/(2n-1)! + x^(2n)/(2n)!
#  Với x là số thực và n là số tự nhiên được nhập từ bàn phím.

isParseDone = False

try:
    x = float(input("Type in a value for x: "))
    n = int(input("Type in a num: "))
    isParseDone = True
except ValueError:
    print("Invalid Input!")

if isParseDone:
    Factorial = 1
    S = 1
    if n > 0:
        for i in range(1, 2*n + 1):
            Factorial *= i
            if i % 2 == 0:
                S += pow(x, i)/Factorial
            else:
                S -= pow(x, i)/Factorial
        print("result: {:.2f}".format(S))
    elif n == 0:
        print("result: {} ".format(1))
    else:
        print("num must be greater than or equal to 0")

        
