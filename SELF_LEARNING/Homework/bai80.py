# Viết hàm với tham số truyền vào là một danh sách. Trả về danh sách các phần tử xuất hiện duy nhất trong danh sách đã cho.

def OnlyOne(array):
    length = len(array)
    if length < 1:
        return None
    else:
        List = [word for word in array if array.count(word) == 1]
        return List

array = input("Input: ").split()
print(*OnlyOne(array))