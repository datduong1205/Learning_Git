# Viết hàm truyền vào tham số là chuỗi s. 
# Nếu ký tự đầu và ký tự cuối của chuỗi s là "*" (hoặc "-") thì  trả về chuỗi s với định dạng title() (hoặc swapcase()). 
# Các trường hợp còn lại trả về chuỗi s với định dạng capitalize().

def ChangeString(S):
    if S.startswith("*") and S.endswith("*"):
        return S.title()
    elif S.startswith("-") and S.endswith("-"):
        return S.swapcase()
    else:
        return S.capitalize()

S = input("String: ")
print(ChangeString(S))