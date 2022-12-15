# Viết hàm với tham số truyền vào là một danh sách các số thực. Kiểm tra xem danh sách có phải là danh sách giảm không.

isParseDone = False
"""
def CheckDecreaseNum(S):
    for num in range(len(S)-1):
        if S[num] < S[num + 1]:
            return False
    return True
"""

def CheckDecreaseNum(S):
    S = all(S[num] >= S[num + 1] for num in range(len(S) - 1))
    return S

def CheckIncreaseNum(S):
    S = all(S[num] <= S[num + 1] for num in range(len(S)-1))
    return S

try:    
    S = list(map(float, input("Input: ").split()))
    isParseDone = True
except ValueError:
    print("Invalid Input!")

if isParseDone:
    print(CheckDecreaseNum(S))
    

