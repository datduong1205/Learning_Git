'''
Viết chương trình làm tròn số thập phân A đến B chữ số sau dấu phẩy.
A và B được nhập bất kỳ từ bàn phím. Hiển thị số A sau khi được làm tròn ra màn hình.
'''
isParseDone = False
A = input("Hãy nhập 1 số thập phân: ")
B = input("Hãy nhập số chữ số muốn hiển thị sau dấu phẩy: ")

try:
    testA = float(A)
    testB = int(B)
    isParseDone = True
except ValueError:
    print("Invalid Value")

if isParseDone:
    print('{0:.{1}f}'.format(testA, testB))

Roundnum = round(testA, testB)
print(Roundnum)