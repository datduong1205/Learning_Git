# Viết chương trình hiển thị ra màn hình các số chia hết cho 5 (không quá 10 số) trong khoảng a, b. 
# Với a, b là hai số nguyên nhập từ bàn phím (a <= b).

isParseDone = False

try:
    a, b = map(int, input("Type in 2 nums: ").split())
    isParseDone = True
except ValueError:
    print("Invalid Input!")

if isParseDone:
    if a > b:
        print("a must be less than b")
    else: 
        count = 0
        for i in range(a, b + 1):
            if i % 5 == 0:
                count += 1
                if count > 10:
                    print("Cannot print over 10 num")
                    break
                print(i, end=" ")
        else:
            if count == 0:
                print("No number is divisible by 5")
            else:
                print("\nDone!")
    
