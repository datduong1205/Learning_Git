# Viết chương trình kiểm tra n có phải số hoàn hoàn thiện không. Với n là số nguyên dương nhập từ bàn phím.

isParseDone = False

try:
    n = int(input("Type in a num: "))
    isParseDone = True
except ValueError:
    print("Invalid Input")

if isParseDone:
    if n > 0:
        sum = 0
        # tổng ước không bao giờ lớn hơn n
        for i in range(1, n//2 + 1):
            if n % i == 0:
                sum += i
        else:
            if sum == n:
                print("{} is a perfect number".format(n))
            else:
                print("{} is not a perfect number".format(n))
    else:
        print("n must be greater than 0")
            