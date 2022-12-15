# Trả về chuỗi s viết thường nếu ký tự đầu chuỗi s là chữ thường. (Tương tự với ký tự viết hoa)

def ChangeCase(S):
    if len(S) == 0:
        return ""
    elif S[0].isupper():
        return S.upper()
    elif S[0].islower():
        return S.lower()
    
S = input("String: ")
print(ChangeCase(S))
