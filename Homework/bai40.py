# Viết chương trình nhập vào từ bàn phím hai số tự nhiên a và b (a <= b). Hiển thị ra màn hình các số nguyên tố trong đoạn từ a đến b.

import math

isParseDone = False

try:
    a, b = map(int, input("Type in 2 nums: ").split())
    isParseDone = True
except ValueError:
    print("Invalid Input!")

if isParseDone:
    if a < 0 or b < 0:
        print("a and b must be greater than 0")
    elif a < 2 and b < 2:
        print("There are no prime numbers from {} to {}".format(a, b))
    else:
        if a <= b:
            for i in range(a, b + 1):
                if i < 2:
                    continue
                for check in range(2, int(math.sqrt(i)) + 1):
                    if i % check == 0:
                        break
                else:
                    print(i, end=" ")   
        else:   
            print("a must be less than b")

                    
    