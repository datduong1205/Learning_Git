# Viết hàm với tham số truyền vào là một danh sách và số nguyên dương n.
# Trả về danh sách kết quả bằng cách chèn phần tử "Hello" vào các vị trí chia hết cho n.

def AddWord(array, n):
    length = len(array)
    if length == 0:
        return None
    else:
        ResultList = []
        for i in range(0, length, n):
            ResultList.extend(array[i:i+n])
            ResultList.append("Hello")
        
        # pop(): default remove and return last element    
        ResultList.pop()
    return ResultList

try:
    array = input("Input: ").split()
    n = int(input("Type in a num: "))
    print(*AddWord(array, n))
except ValueError:
    print("Invalid Input!")
