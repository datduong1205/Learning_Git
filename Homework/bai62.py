# Viết hàm nối các từ của chuỗi s bằng dấu "-"

def ConnectWord(S):
    S = S.split()
    S = "-".join(S)
    return S

S = input("String: ")
print(ConnectWord(S))