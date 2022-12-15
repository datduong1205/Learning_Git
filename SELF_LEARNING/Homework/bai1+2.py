#Viết chương trình tính và hiển thị ra màn hình tổng hai số nguyên được nhập bất kỳ từ bàn phím

a = int(input("Hãy nhập số đầu tiên: "))
b = int(input("Hãy nhập số thứ hai: "))
sum1 = a + b

print("Tổng 2 số đã nhập là:  " + str(sum1))



#Viết chương trình tính và hiển thị ra màn hình tổng hai số nguyên được nhập bất kỳ từ bàn phím (Có xử lý ngoại lệ đầu vào).

try:
    c = int(input("Hãy nhập số thứ ba: "))
    d = int(input("Hãy nhập số thứ tư: "))
    print(c + d)
except ValueError:
    print("Invalid Input")
