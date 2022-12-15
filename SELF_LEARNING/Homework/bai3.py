# Viết chương trình hiển thị các từ theo yêu cầu ra màn hình: “Xin”, “chao!", “Toi", “ten", “la”, “{Tên của bạn}”.
# Các từ cách nhau bởi “--” và {Tên của bạn} được nhập từ bàn phím.

name = input("Tên: ")

print("Xin", "chao!", "toi", "ten", "la", name, sep='--')

def birthday(day, month, year):
    print("I was born on ")
    print(str(day), str(month), str(year), sep='/')

if name == "Dat":
    birthday(12, 5, 2004)
elif name == "Tran":
    birthday(21, 5 ,2004)