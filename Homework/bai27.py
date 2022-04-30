# Viết chương trình hiển thị ra màn hình bảng cửu chương n. Với n là số tự nhiên từ 1 đến 9 nhập từ bàn phím.

isParseDone = False

try:
    n = int(input("Type in a num from 1 to 9: "))
    isParseDone = True
except ValueError:
    print("Invalid Input!")

if isParseDone:
    if n in range(10):
        for i in range(1, 11):
            print("{} * {} = {}".format(n, i, n * i))
        else:
            print("Done!")
    else:
        print("Num must be from 1 to 9")

    print(i, end="")
        


