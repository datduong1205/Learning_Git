# Viết chương trình hiển thị ra màn hình tất cả các ước của một số tự nhiên n nhập từ bàn phím.

isParseDone = False

try:
    n = int(input("Type in a num: "))
    isParseDone = True
except ValueError:
    print("Invalid Input")

if isParseDone:
    if n > 0:
        for i in range(1, n +1):
            if n % i == 0:
                print(i, end=" ")
    else:
        print("n must be greater than 0")
