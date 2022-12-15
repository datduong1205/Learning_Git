# Viết hàm với tham số truyền vào là hai danh sách số thực có cùng kích thước.
# Trả về danh sách kết quả bằng cách nhân lần lượt số đầu tiên của danh sách 1 với số cuối cùng của danh sách 2 cho tới hết danh sách.

def MultiplyList(List1, List2):
    ResultList = [num1*num2 for num1, num2 in zip(List1, List2[::-1])]
    return ResultList

List1 = input("List1: ").split()
List2 = input("List2: ").split()

if len(List1) == len(List2):
    try:
        List1 = list(map(float, List1))
        List2 = list(map(float, List2))
        ResultList = MultiplyList(List1, List2)
        print(*ResultList)
    except ValueError:
        print("Invalid Input!")
else:
    print("length of list must be the same!")