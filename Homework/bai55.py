# Viết hàm truyền vào tham số là hai chuỗi s1 và s2.
#  Trả về chuỗi kết quả bằng cách đan xen lần lượt ký tự đầu của chuỗi s1 và ký tự cuối của chuỗi s2 cho đến hết chuỗi.

def MixString(A, B):
    ReverseB = B[::-1]
    GreaterLen = max(len(A), len(B))
    Result = "" 
    for i in range(GreaterLen):
        if i < len(A):
            Result += A[i]
        if i < len(B): 
            Result += ReverseB[i]
    return Result

A = input("Input1: ")
B = input("Input2: ")

print(MixString(A, B))