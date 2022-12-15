# Viết chương trình hiển thị ra màn hình tam giác số kích thước n theo mẫu (Phần 2).
#  Với n là số tự nhiên từ 1 đến 9 nhập từ bàn phím.

isParseDone = False

try:
    n = int(input("Type in num from 1 to 9: "))
    isParseDone = True
except ValueError:
    print("Invalid Input!")


if isParseDone:
    if n in range(1, 10):
        for row in range(n):
            for column in range(n-row, 0, -1):
                print(column, end=" ")
            print()
    else:
        print("Only accept num from 1 to 9!")
