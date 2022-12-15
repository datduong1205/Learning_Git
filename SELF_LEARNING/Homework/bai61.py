# Viết hàm truyền vào tham số là chuỗi s.
#  Trả về số lượng các ký tự nguyên âm và chuỗi s sau khi đã thay thế các ký tự nguyên âm bằng ký tự "$".

def ReplaceVowel(S):
    Vowels = "ueoaiUEOAI"
    count = 0
    for i in Vowels:
        count += S.count(i)
        S = S.replace(i, "$")
    return S

S = input("Strimg: ")
print(ReplaceVowel(S))

