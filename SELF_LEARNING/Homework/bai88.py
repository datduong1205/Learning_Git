# Viết hàm trả về danh sách gồm các phần tử riêng của hai danh sách (Tham số là 2 danh sách).

def UniqueList(List1, List2):
    List1Result = [a for a in List1 if a not in List2]
    List2Result = [b for b in List2 if b not in List1]
    FinalResult = List1Result + List2Result
    return FinalResult

List1 = input("Input: ").split()
List2 = input("Input: ").split()

FinalResult = UniqueList(List1, List2)
print(*FinalResult)
