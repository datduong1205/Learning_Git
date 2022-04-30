'''			TUPLE			'''

# được giới hạn bởi 1 cặp ngoặc ()
# các phần tử của Tuple được phân cách nhau bởi dấu ,
# Tuple có khả năng chứa mọi giá trị
# tốc độ truy xuất của Tuple nhanh hơn List
# dung lượng chiếm trong bộ nhớ nhỏ hơn List
# bảo vệ dữ liệu của bạn sẽ không bị thay đổi
# có thể dùng làm KEY của DICTIONARY

# tuple cũng có ma trận
tup = (1,2,3,'York University', (4,5,6),['Dat'])
print(tup)

# trường hợp này Python không tính là 1 Tuple
# thêm dấu phẩy để Python biết là Tuple
a = (1)
print(a)

	# tuple generator expression
# tạo ra 1 danh sách các phần tử
b = (i for i in range(10) if i % 2 == 0)
print(tuple(b))

	# tuple constructor
# tạo ra 1 tuple
c = tuple([1,2,3,('Dat')])
print(c)

TUP = (2,4,6,8)
TUP += (1,3,5,7)
print(TUP)

TUP *= 2
print(TUP)

d = 10 in TUP 
print(d)


print(TUP[1])

# đếm số phần tử có trong TUP
print(len(TUP))

print(TUP[-1])

# đảo ngược phần tử
print(TUP[::-1])

#TUP[0] = 'Dat' : lỗi

e = tup.count(['Dat'])
print(e)

f = tup.index(3)
print(f)