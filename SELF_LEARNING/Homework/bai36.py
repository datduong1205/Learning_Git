# Viết chương trình tính và hiển thị ra màn hình số Fibonacci thứ n. Với n là số tự nhiên nhập từ bàn phím

isParseDone = False

try:
    n = int(input("type in a num: "))
    isParseDone = True
except ValueError:
    print("Invalid Input!")

if isParseDone:
    if n > 0:
        if n == 1 or n == 2:
            print("Fibonacci: {}".format(1))
        else:
            x1, x2 = 1, 1
            for i in range(n-2):
                x1 ,x2 = x2, x1 + x2
            print("Fibonacci: {}".format(x2))
    else:
        print("n must be greater than 0")        

