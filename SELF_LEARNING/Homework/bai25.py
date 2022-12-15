# Viết chương trình nhập vào bàn phím hai số nguyên a và b (a <= b). Tính và hiển thị ra màn hình tổng các số trong khoảng a đến b. 

a, b = map(int, input("Type in 2 numbers: ").split())

try:
    if a>b:
        print("a must be smaller than b")
    else:
        sum = 0
        for i in range(a, b+1):
            sum += i
        print(sum)
except ValueError:
    print("Invalid Input!")
