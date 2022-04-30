# Viết chương trình hiển thị ra màn hình tam giác số kích thước n theo mẫu.
#  Với n là số tự nhiên từ 1 đến 9 nhập từ bàn phím.

isParseDone = False

try:
    n = int(input("Type in a num from 1 to 9: "))
    isParseDone = True
except ValueError:
    print("Invalid Input!")

if isParseDone:
    if n in range(1, 10):
        for row  in range(1, n+1):
            for column in range(1, row+1):
                print(column, end=" ")
            # \n 
            print()
    else:
        print("num must be from 1 to 9!")