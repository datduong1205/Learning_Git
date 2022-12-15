a = 2
print(a) 
print(type(a))

# lấy toàn bộ nội dung của thư viện decimal
from decimal import* # * là mọi thứ

# lấy tối đa 30 chữ số phần nguyên và phần thập phân Decimal
getcontext().prec = 30
# type để xem kiểu của số
b = 10/3
print(b)
print(type(b))

c = Decimal(10)/Decimal(3)
print(c)
print(type(c))

# phân số
from fractions import*

frac1 = Fraction(6,9) # tử 6 mẫu 9
frac2 = Fraction(9,12)
frac3 = frac1 + frac2

print(frac3)
print("-----")

# số phức (complex)
# <phần thực> + <phần ảo>j

d = complex(2,5)
print(d.real) # lấy phần thực
print(d.imag) # lấy phần ảo

print(10//3) # chia lấy phần nguyên
print(10%3)  # chia lấy phần dư
print(10**3) # 10 mũ 3

import math # lấy nội dung của thư viện toán học

print(math.sqrt(4)) # lấy căn bậc 2

print(math.trunc(3.10)) # lấy phần nguyên

print(math.floor(3.10)) # làm tròn xuống

print(math.ceil(3.10))  # làm tròn lên

print(math.fabs(-10))   # lấy trị tuyệt đối

print(math.gcd(100,50)) # ước chung lớn nhất