# Viết hàm xóa các ký tự trùng lặp trong chuỗi. (Tham số truyền vào là chuỗi s).

def PopSameWord(S):
    result = ""
    for i in S:
        if i not in result:
            result += i

    return result

S = input("String: ")
print(PopSameWord(S))