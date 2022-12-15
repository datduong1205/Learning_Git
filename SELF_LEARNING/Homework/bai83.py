# Viết hàm với tham số truyền vào là một danh sách các số thực.
# Trả về giá trị, số lượng và vị trí xuất hiện của phần tử lớn nhất trong danh sách.

def MaxElement(array):
    length = len(array)
    if length < 1:
        return None
    else:
        BiggestValue = max(array)
        Amount = array.count(BiggestValue)
        idxNum = [num for num in range(0, len(array)) if array[num] == BiggestValue ]
        return BiggestValue, Amount, idxNum

try:
    array = list(map(float, input("Array: ").split()))
    BiggestValue, Amount, idxNum = MaxElement(array)
    print(BiggestValue)
    print(Amount)
    print(*idxNum)
except ValueError:
    print("Invalid Input!")



