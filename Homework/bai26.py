# Viết chương trình nhập vào bàn phím hai số nguyên a và b (a <= b). Tính và hiển thị ra màn hình tổng các số trong khoảng a đến b.
# Yêu cầu sử dụng vòng lặp while.

isParseDone = False

try:
    a, b = map(int, input("Type in 2 numbers: ").split())
    isParseDone = True
except ValueError:
    print("Invalid Input!")


if isParseDone:
    if a > b:
        print("a must be smaller than b")
    else:
        sum = 0
        i = a
        while i <= b:
            sum += i
            i += 1
        print(sum)

