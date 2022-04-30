# Viết chương trình nhập vào từ bàn phím tên và chiều cao (cm) của hai bạn. Hiển thị ra màn hình thông báo bạn nào cao hơn.(có xử lý ngoại lệ)


isParseDone = False 
first = input("type in your name and height: ").split()
second = input("type in your name and height: ").split()

try:
    height1 = int(first[1])
    height2 = int(second[1])
    isParseDone = True
except ValueError:
    print("Invalid Input")


if isParseDone:
    if height1 <= 0 or height2 <= 0:
        print("Height must be higher than 0")
    else:
        if height1 > height2:
            print("{} is higher than {}".format(first[0], second[0]))
        elif height1 < height2:
            print("{} is higher than {}".format(second[0], first[0]))
        else:
            print("Both height are the same")


