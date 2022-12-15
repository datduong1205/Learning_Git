# Viết hàm với tham số truyền vào là một danh sách và số tự nhiên n.
# Trả về danh sách n phần tử bằng cách lặp lại danh sách được truyền vào.

def CloneArray(array, n):
    length = len(array)
    CloneTimes = n // length + 1
    CloneList = array * CloneTimes
    ArrayList = CloneList[:n]
    return ArrayList

array = input("Input: ").split()
if len(array) == 0:
    print("Empty Input!")
else:
    try:
        n = int(input("Input: "))
        ResultList = CloneArray(array, n)
        print(*ResultList)
    except ValueError:
        print("Invalid Input!")
