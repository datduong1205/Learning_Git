# Viết hàm với tham số truyền vào là một danh sách các số thực. 
# Trả về trung bình cộng và hai danh sách: một danh sách gồm các số nhỏ hơn
# và một danh sách gồm các số lớn hơn hoặc bằng trung bình cộng của danh sách được truyền vào.

isParseDone = False

def SplitList(NumList):
    Average = sum(NumList) / len(NumList)
    LessThanAverageList = [a for a in NumList if a < Average]
    GreaterThanAverageList = [b for b in NumList if b >= Average]
    return Average, LessThanAverageList, GreaterThanAverageList

NumList = input("Enter a string of numbers: ").split()

try:
    isParseDone = True
    NumList = list(map(float, NumList))
except ValueError:
    print("Invalid Input!")

if isParseDone:
    Average, LessThanAverageList, GreaterThanAverageList = SplitList(NumList)
    print(Average)
    print(*LessThanAverageList)
    print(*GreaterThanAverageList)