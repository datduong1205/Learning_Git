# Viết hàm với tham số truyền vào là một danh sách các số thực. Trả về trung bình cộng của danh sách đó.

def AverageNum(S):
    total_S = sum(S)
    Average = total_S/len(S)
    return Average

try:
    S = list(map(float, input("Input: ").split()))
    if len(S) == 0:
        print("Empty Input!")
    else:
        print(AverageNum(S))
except ValueError:
    print("Invalid Input!")