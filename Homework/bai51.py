# Viết hàm liệt kê các số hoàn thiện nhỏ hơn m.

def CheckPerfectNum(m):
    sum = 0
    for i in range(1, m // 2 +1):
        if m % i == 0:
            sum += i  
    if sum == m:
        return True
    else:
        return False

def PerfectNum(n):
    for i in range(1, n):
        if CheckPerfectNum(i):
            print(i, end=" ")

isParseDone = False

try:
    n = int(input("Type in 1 num: "))
    isParseDone = True
except ValueError:
    print("Invalid Input!")
    
if isParseDone:    
    if n > 0:
        PerfectNum(n)
    else:
        print("n must be greater than 0")

