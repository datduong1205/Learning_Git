# Viết hàm trả về hai danh sách sau khi đã hoán đổi nữa sau danh sách cho nhau. (Tham số là 2 danh sách bất kỳ).

def ConvertList(List1, List2):
    HalfLengthList1 = len(List1) // 2
    HalfLengthList2 = len(List2) // 2
    HalfList1 = List1[HalfLengthList1:]
    HalfList2 = List2[HalfLengthList2:]
    List1 = List1[:HalfLengthList1] + HalfList2
    List2 = List2[:HalfLengthList2] + HalfList1
    return List1, List2  

List1 = input("Type in: ").split()
List2 = input("Type in: ").split()

ConvertList1, ConvertList2 = ConvertList(List1, List2)
print(*ConvertList1)
print(*ConvertList2)