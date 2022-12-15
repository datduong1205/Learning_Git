# Viết hàm truyền vào tham số là chuỗi s. Hiển thị số lần xuất hiện của các ký tự trong chuỗi s.

def PopSameWord(S):
    ResultString = ""
    for word in S:
        if word not in ResultString:
            ResultString += word
    return ResultString

def CountWord(S):
    WordSequence = PopSameWord(S)
    for word in WordSequence:
        Count = S.count(word)
        print("{}: {};".format(word, Count), end=" ")

    
S = input("Sequence: ")
CountWord(S)
