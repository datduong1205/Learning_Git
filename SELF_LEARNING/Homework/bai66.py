# Viết hàm truyền vào tham số là chuỗi s. Hiển thị các câu của chuỗi s, mỗi câu nằm trên một dòng.
#  Các câu đã được xóa khoảng trắng thừa và căn giữa theo câu dài nhất.

def Requirement(S):
    S = S.strip()
    while "  " in S:
        S = S.replace("  ", " ")

    S = S.split(". ")

    TheLongestWord = ""
    for Word in S:
        if (len(Word) > len(TheLongestWord) or len(Word) == len(TheLongestWord) and Word < TheLongestWord ):
            TheLongestWord = Word

    for i in S:
        print(i.center(len(TheLongestWord)))

S = input("String: ")
Requirement(S)

