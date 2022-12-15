# Viết hàm trả về list các ký tự theo thứ tự đảo ngược của chuỗi s.

def ReversedList(S):
    CharaterList = list(S)
    ReversedCharacterList = CharaterList[::-1]
    return ReversedCharacterList

S = input("Input: ")

ReversedCharacterList = ReversedList(S)
print(*ReversedCharacterList)