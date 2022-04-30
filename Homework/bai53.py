# Viết hàm truyền vào tham số là hai chuỗi s1 và s2. Kiểm tra chuỗi s2 có xuất hiện trong chuỗi s1 không
#  nếu không thì hiển thị thông báo, nếu có thì hiển thị số lần xuất hiện.

def String(a, b):
    if b in a:
        return a.count(b)
    else:
        return "{} not in {}".format(b, a)


a = input("Type in anything: ")
b = input("Type in anything: ")

print(String(a, b))