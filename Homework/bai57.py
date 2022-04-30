# Viết hàm truyền vào tham số là chuỗi s. Trả về chuỗi kết quả bằng cách xóa các ký tự chẵn (hoặc lẻ) nếu chuỗi s có độ dài là một số chẵn (hoặc lẻ) (vị trí chuỗi bắt đầu từ 0).

def CutString(S):
    FinalString = ""
    for i in range(len(S)):
        if i % 2 != len(S) % 2:
            FinalString += S[i]
    return FinalString

S = input("Input: ")
print(CutString(S))


