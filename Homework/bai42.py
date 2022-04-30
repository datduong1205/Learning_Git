# Viết hàm trả về tên của bạn có chiều cao lớn hơn trong hai bạn. Với tham số là tên và chiều cao của hai bạn.

isParseDone = False

def Name_Height(Name1, Height1, Name2, Height2):
    if Height1 > 0 and Height2 > 0:
        if Height1 > Height2:
            print("{} is taller than {}".format(Name1, Name2))
        elif Height1 < Height2:
            print("{} is taller than {}".format(Name2, Name1))
        else:
            print("{} and {} are at the same height".format(Name1, Name2))
    else:
        print("Height must be greater than 0")

try:
    Name1, Name2 = map(str, input("Type in 2 names: ").split())
    Height1, Height2 = map(int, input("Type in 2 heights: ").split())
    isParseDone = True
except ValueError:
    print("Invalid Input!")

if isParseDone:
    Name_Height(Name1, Height1, Name2, Height2)
        

