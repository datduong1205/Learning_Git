# Viết chương trình nhập vào từ bàn phím một số bất kỳ ở hệ thập phân và hiển thị ra màn hình số đó ở hệ bát phân.

sothapphan1 = int(input("Hãy nhập 1 số: "))
print("Số thập phân %d trong hệ bát phân là: %o " % (sothapphan1, sothapphan1))


# Viết chương trình nhập vào từ bàn phím một số bất kỳ ở hệ thập phân và hiển thị ra màn hình số đó ở hệ bát phân 
# (Có xử lý ngoại lệ đầu vào).


sothapphan2 = input("Hãy nhập 1 số: ")
isParseDone = False

try:
    test = int(sothapphan2)
    isParseDone = True
except ValueError:
    print("Invalid Input!")

if isParseDone:
    print("Số thập phân %d ở hệ bát phân là: %o" %(test, test))




