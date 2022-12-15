# Viết chương trình giải phương trình bậc hai với các hệ số được nhập từ bàn phím và hiển thị kết quả ra màn hình.(có xử lý ngoại lệ)

# thư viện Math để sử dụng hàm sqrt tính  căn bậc 2
import math

isParseDone = False

try:
    a, b, c = map(float, input("Type in 3 coefficients:").split())
    isParseDone = True
except ValueError:
    print("Invalid Input!")


if isParseDone:
    delta = b**2 - 4*a*c

    if a == 0:
        if b == 0:
            if c == 0:
                print("The equation has infinite solutions")
            else: 
                print("The equation has no solution")
        else:
            print("The equation has 1 solution: \n x = {}".format(-c/b))
    else:
        if delta < 0:
            print("The equation has no solution")
        elif delta == 0:
            x = -b / (2*a)
            print("The equation has 2 same solutions: \n x1 = x2 = {} ".format(x))
        elif delta > 0:
            x1 = float((-b + math.sqrt(delta))/(2*a))
            x2 = float((-b - math.sqrt(delta))/(2*a))
            print("The equation has 2 distinc solutions: \n x1 = {} \n x2 = {}".format(x1, x2))