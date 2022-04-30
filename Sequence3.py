	# phần 5
A = '1221052004'
a = 'York University - IT'
print(a)

# .split cắt từng từ theo yêu cầu (từ trái qua), cắt từ phải: .rsplit()
b = a.split(' ', 2)
print(b)
print(a.rsplit(' ', 2))

# .partition cắt ra thành 3 phần tử trước và sau + chuỗi được chọn
# .rpartition cắt từ bên phải
c = a.partition('r')
print(c)
print(a.rpartition('r '))

# .count: đếm 
d = a.count('r',0,3)
print(d)

# .startswith: xuất phát bằng ?
e = a.startswith('r',2,12)
print(e)

# .endswith: kết thúc bằng ?
f = a.endswith('T')
print(f)

# .find: tìm vị trí và trả ra số là vị trí đầu tiên
g = a.find('University')
print(g)
print(a.rfind('Y'))

# .index: tương tự như find, nếu tìm không thấy sẽ báo lỗi
h = a.index('o')
print(h)

# .islower: có phải toàn bộ nỗi dung viết thường không ? (TRUE/FALSE)
i = a.islower()
print(i)

# .isupper: có phải toàn bộ nỗi dung viết hoa không ? (TRUE/FALSE)
j = a.isupper()
print(j)

# .isdigit: có phải toàn bộ là số không? (TRUE/FALSE)
k = A.isdigit()
print(k)

# .isspace: có phải toàn bộ chuỗi là khoảng trắng? (TRUE/FALSE)
l = a.isspace()
print(l)

