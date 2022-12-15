'''
try:
	a = int(input("Hay nhap so thu nhat: "))
	b = int(input("Hay nhap so thu hai: "))
	c = int(input("Hay nhap so thu ba: "))
	if a > b and a > c:
		print("số lớn nhất là: ", a)
	elif b > a and b > c:
		print("Số lớn nhất là: ",b)
	else:
		print("Số lớn nhất là: ", c)
except ValueError:
	print("Invalid Input")
'''

'''
from types import DynamicClassAttribute


five_even_numbers = []
number = 1 

while len(five_even_numbers) < 5:
	if number % 2 == 0:
		five_even_numbers.append(number)
	number += 1

print(five_even_numbers)
'''

'''
with open("draft.txt") as f:
	# lấy nội dung của file dưới dạng list 
	data = f.readlines()

idx = 0 # mốc bắt đầu
length = len(data) # mốc kết thúc
new_content = "" # nội dung mới sẽ được ghi vào file mới

while idx < length:
	# tách một dòng thành 1 list
	line_list = data[idx].split()
	idline = 0
	length_line = len(line_list)
	while idline < length_line:
		if line_list[idline] == "Kteam": 
			line_list[idline - 1] = "How"
		idline += 1
	# nối lại thành 1 dòng chuỗi 
	new_content += " ".join(line_list) + "\n"
	idx += 1

with open("Dat.txt", "w") as new_f:
	# ghi nội dung mới vào file 
	new_f.write(new_content)
'''


'''
lst = [56, 14, 11, 756, 34, 90, 11, 11, 65, 0, 11, 35]

idx = 0
maidx = len(lst) - 1

majdx = len(lst)

while idx < maidx:
	if lst[idx] == 11:
		idx += 1
		continue
	jdx = idx + 1
	while jdx < majdx:
		if lst[jdx] == 11:
			jdx += 1
			continue
		if lst[idx] > lst[jdx]:
			lst[idx], lst[jdx] = lst[jdx], lst[idx]
		jdx += 1
	idx += 1

print(lst)


Lst = [[1, 2, 3], [4, 5, 6]]

for value in Lst:
	value[0] = None

print(Lst)
'''

'''
n = int(input("Enter size of matrix: "))

dx, dy = 1, 0
x, y = 0, 0

spiral_matrix = [[None] * n for j in range(n)]

for i in range(n ** 2):
	spiral_matrix[x][y] = i
	nx, ny = x + dx, y 
	if 0 <= nx < n and 0 <= ny < n and spiral_matrix[nx][ny] == None:
		x, y = nx, ny
	else:
		dx, dy = -dy, dx
		x, y = x + dx, y + dy

for y in range(n):
	for x in range(n):
		print("%02i" % spiral_matrix[x][y], end= " ")
	print()

print()
'''

'''
def f_x(x):
	return x**3 + 2*x**2 -4*x + 1


def check_point(x, y):
	if y == f_x(x):
		return True
	return False

def fil_point(lst_point):
	lst_A, lst_B = [], []
	for l in main_list:
		if check_point(*l):
			lst_A.append(l)
			continue
		lst_B.append(l)
	return lst_A, lst_B

def cal_sum(main_list):
	s = 0
	for value in main_list:
		s += value[1]
	return s



main_list = [(-5, -20), (-4, -15), (-3, 4), (-2, 9), (-1, 7), (0, 1), (1, -7), (2, -9), (4, 81), (5, 130)]

lst_A_after, lst_B_after = fil_point(main_list)
print(abs(cal_sum(lst_A_after) - cal_sum(lst_B_after)))

a = 32 
b = 59
c = 8
d = 24
e = 15

def f_max(x, y):
	return int((x+y + abs(x - y))/2)

_max = f_max(f_max(f_max(f_max(a, b), c), d), e)

print(2 * _max - 1)

a = input().split()
print(a)
'''
hi = "*" * 4
print(hi)
