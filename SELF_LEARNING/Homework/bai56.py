# Viết hàm truyền vào tham số là chuỗi s. Trả về chuỗi kết quả bằng cách thay thế đuôi "ing" bằng đuôi "ly" nếu chuỗi s kết thúc bằng "ing", nếu không thì thêm đuôi "ing" vào chuỗi s.

def ChangeForm(S):
    if len(S) < 3 or S[-3:] != "ing":
        S += "ing"
    else:
        S = S[:-3] + "ly"
    return S

s = input("Input: ")
print(ChangeForm(s))