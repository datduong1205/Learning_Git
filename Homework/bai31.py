# Viết chương trình hiển thị ra màn hình tam giác cân chứa các ký tự alphabet kích thước n theo mẫu.
#  Với n là số tự nhiên nhập từ bàn phím.

isParseDone = False

try:
    n = int(input("Type in 1 num: "))
    isParseDone = True
except ValueError:
    print("Invalid Input!")

if isParseDone:
    if n > 0:
        Ascii = 65
        for i in range(n):
            Blank = " "*((n-i)*2 - 1)
            print(Blank, end=" ")
            for j in range(2*i + 1):
                Case = chr(Ascii)
                print(Case, end=" ")
                Ascii += 1 
                if chr(Ascii) > "Z":
                    Ascii = 65
            print() 
    else:
        print("num must be greater than 0")
