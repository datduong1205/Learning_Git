# Viết hàm với tham số truyền vào là chuỗi s. Trả về tổng và trung bình cộng của các từ là số tự nhiên trong chuỗi s.

def AverageResult(S):
    S = S.split()
    Sum = 0
    Count = 0
    for i in S:
        if i.isdigit():
            Sum += int(i)
            Count += 1
    if Count == 0:
        return 0, 0
    Average = Sum / Count
    return Sum, Average

S = input("Input: ")
Sum, Average = AverageResult(S)

print(Sum)
print(Average)