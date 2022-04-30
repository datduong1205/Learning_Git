# Hàm liệt kê số nguyên tố trong đoạn từ A đến B. (a,b là số tự nhiên, a<=b)

import math

def CheckPrimeNum(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def PrimeNum(a, b):
    for i in range(a, b + 1):
        if CheckPrimeNum(i):
            print(i, end=" ")


try:
    a, b = map(int, input("Type in 2 nums: ").split())
    if a < 0 or b < 0:
        print("a and b must be greater than 0")
    elif a < 2 and b < 2:
        print("There are no prime nums from {} to {}".format(a, b))
    else:
        PrimeNum(a, b)
except ValueError:
    print("Invalid Input!")