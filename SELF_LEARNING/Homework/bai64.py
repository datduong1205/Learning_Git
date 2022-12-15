# Hàm trả về từ có độ dài lớn nhất theo thứ tự trong chuỗi s. (Tham số truyền vào là chuỗi s).

def LongestWord(S):
    TheLongestWord = ""
    WordList = S.split()
    for word in WordList:
        if (len(word) > len(TheLongestWord) or len(word) == len(TheLongestWord) and word < TheLongestWord):
            TheLongestWord = word 

    return TheLongestWord

S = input("String: ")
print(LongestWord(S))
