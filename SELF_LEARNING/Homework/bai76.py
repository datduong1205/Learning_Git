# Viết hàm với tham số truyền vào là một danh sách các số nguyên. Trả về danh sách các phần tử lẻ.

isParseDone = False
"""
def odd_num(S):
    oddNumber = []
    for num in S:
        if num % 2 == 1:
            oddNumber.append(num)
    return oddNumber

try:
    S = list(map(int, input("Input: ").split()))
    isParseDone = True
except ValueError:
    print("Invalid Input!")

if isParseDone:
    if len(S) == 0:
        print("Empty Input!") 
    else:
        print(*odd_num(S))
"""

def odd_num(S):
    oddnumber = [num for num in S if num % 2 != 0]
    return oddnumber

try:
    isParseDone = True
    S = list(map(int, input("Input: ").split()))
except ValueError:
    print("Invalid Input!")


if isParseDone:
    if len(S) == 0:
        print("Empty Input!")
    else:
        print(*odd_num(S))
