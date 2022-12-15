# Viết hàm truyền vào tham số là chuỗi s.
#  Hiển thị các câu của chuỗi s, mỗi câu nằm trên một dòng. Các câu đã được xóa khoảng trắng thừa và định dạng title().

def Requirement(S):
    S = S.strip()
    while "  " in S:
        S = S.replace("  ", " ")

    S = S.split(". ")
    for i in S:
        print(i.title())


S = input("String: ")
Requirement(S)
