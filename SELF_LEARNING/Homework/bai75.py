# Viết hàm với tham số truyền vào là một danh sách các số thực. Trả về phần tử có giá trị nhỏ nhất (Không dùng hàm min).

def min_num(S):
    lowestnum = S[0]
    for num in S:
        if num < lowestnum:
            lowestnum = num
    return lowestnum

try:
    S = list(map(float, input("Input: ").split()))
    if len(S) == 0:
        print("Empty Input!")
    else:
        print(min_num(S))
except ValueError:
    print("Invalid Input!")