# Viết chương trình kiểm tra n có phải số nguyên tố không. Với n là số tự nhiên nhập từ bàn phím.

import math 

isParseDone = False

try:
    n = int(input("Type in a num: "))
    isParseDone = True
except ValueError:
    print("Invalid Input!")

if isParseDone:
    if n < 0:
        print("n must be greater than 0")
    elif n < 2:
        print("{} is not a prime number".format(n))
    else:
        # chỉ cần duyệt tới căn bậc 2 của n, không cần duyệt tới 1 nửa
        
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                print("{} is not a prime number".format(n))
                break
        else:
            print("{} is a prime number".format(n))