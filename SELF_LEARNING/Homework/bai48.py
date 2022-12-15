# Viết hàm tính n giai thừa (n!)


def factorial(n):
    if n > 0:
        Result = 1
        for i in range(1, n+1):
            Result *= i
        return "factorial of {} is: {}".format(n, Result)
    else:
        return "n must be greater than 0"

isParseDone = False

try:
    n = int(input("Type in 1 num: "))
    isParseDone = True
except ValueError:
    print("Invalid Input!")

if isParseDone:
    print(factorial(n))