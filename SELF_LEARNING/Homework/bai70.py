#Viết hàm với tham số truyền vào là chuỗi s. Trả về số lượng từ vừa chứa ký tự, vừa chứa chữ số trong chuỗi s.

def Digit_Char_Sentence(S):
    word_list = S.split()
    Count = 0
    for sentence in word_list:
        CharConfirmed = False
        DigitConfirmed = False

        for word in sentence:
            if word.isalpha():
                CharConfirmed = True
            
            if word.isdigit():
                DigitConfirmed = True
            
        if CharConfirmed and DigitConfirmed:
            Count += 1

    return Count

S = input("Input: ")

print(Digit_Char_Sentence(S))

    
            
