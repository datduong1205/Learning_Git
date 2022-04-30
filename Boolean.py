
print(2 <= 5)

print(3>1 & 1>3)

print(69 != 10)

print(241 == (141 + 100))

print((5 * 0) != 0)

print("DatDuong" == "DatDuong")

print("VietNam" != "America")

# Python đổi ký tự thành số để so sánh
# chỉ có thể lấy số của từng ký tự
print(ord("B"))

o1 = ord("a")
o2 = ord("A")
print(o1)
print(o2)

print(o1 > o2)

print("aaa" < "AAAaaa")

print("aaa" < "aaacv")


lst = [1, 2, 3]
lst_ = [1, 2, 3]

print(lst == lst_) #True

# khi dùng is, python sẽ so sánh theo id
print(lst is lst_) #False

_lst = lst_

print( _lst is lst_) #True


# các số từ -5 đến 256 
# chuỗi có số ký tự dưới 20 
# các biến có cùng 1 giá trị sẽ có cùng 1 giá trị trả về từ hàm id

a = -5
b = -5
print(a is b) #True

c = 256
d = 256 
print(c is d) #True

# bản chất: True = 1, False = 0
print(int(True))
print(int(False))

a = 5 

print(1 < a < 6) #True


k = 4 

print(k == 3 or k == 4 or k == 5) #True

print(k in (3, 4, 5)) #True
