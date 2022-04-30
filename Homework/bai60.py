# Viết hàm truyền vào tham số là chuỗi s. Trả về chuỗi s sau khi được xóa các khoảng trắng thừa.

def ReplaceSpace(S):
    S = S.strip()
    while "  " in S:
        S = S.replace("  ", " ") 
    return S

S = input("String: ")
print(ReplaceSpace(S))