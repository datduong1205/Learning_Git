# Viết hàm truyền vào tham số là chuỗi s và hai số tự nhiên a, b (a <= b).
# Trả về chuỗi con đảo ngược từ vị trí a đến vị trí b của chuỗi s (vị trí của chuỗi bắt đầu từ 0).

def ReverseString(S, a, b):
    ChildString = S[a:b+1]
    ReverseChildString = ChildString[::-1]
    return ReverseChildString

try:
    S = input("Type in: ")
    a, b = map(int, input("Type in 2 nums: ").split())
    if a < 0 or b < 0:
        print("a and b must be greater than 0")
    elif a >= b:
        print("a must be less than b")
    elif a >= len(S) or b >= len(S):
        print("a and b must be less than {}".format(len(S)))
    else:
        print(ReverseString(S, a, b))
except ValueError:
    print("Invalid Input! ")