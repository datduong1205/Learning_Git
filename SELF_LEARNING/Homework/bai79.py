# Viết hàm với tham số truyền vào là một danh sách các số nguyên dương.
# Trả về danh sách các phần tử là số nguyên tố.

import math
isParseDone = False

def PrimeNumberCheck(n):
    if n < 1:
        return False
    else:
        for i in range(2, int(math.sqrt(n)+1)):
            if n % i == 0:
                return False
    return True

def PrimeNumberArray(array):
    Prime = [num for num in array if PrimeNumberCheck(num)]
    return Prime

try:
    isParseDone = True
    array = list(map(int, input("Squence Number: ").split()))
except ValueError:
    print("Invalid Input!")

if isParseDone:
    print("Prime Number: ", *PrimeNumberArray(array))