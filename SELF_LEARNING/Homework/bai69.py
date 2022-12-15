# Viết hàm với tham số truyền vào là chuỗi s.
# Trả về số lượng chữ số, số lượng ký tự, số lượng ký hiệu và chuỗi s được sắp xếp thành ba phần theo thứ tự chữ số, ký tự, ký hiệu.

def digit_char_symbol(S):
    digit_list = ""
    char_list = ""
    symbol_list = ""
    for i in S:
        if i.isupper() or i.islower():
            char_list += i
        elif i.isdigit():
            digit_list += i
        else:
            symbol_list += i
    
    StringSorted = digit_list + char_list + symbol_list
    return len(digit_list), len(char_list), len(symbol_list), StringSorted  


S = input("Input:" )

digit, char, symbol, sortedstring = digit_char_symbol(S)

print(digit, char, symbol, sep="\n")
print(sortedstring)