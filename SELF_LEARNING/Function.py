# hàm phải có ()
# biến không cần

def BaoTran(): 
	print("Hello BaoTran! ")

BaoTran()

def MinhDat(text, age):
 	print(text)
 	print(age)

MinhDat("Hello MinhDat! ", 69)

# default argument bắt buộc nằm cuối
def DatTran(date, text = "Lover"):
	print(date)
	print(text)

# không truyền giá trị, text sẽ lấy default
DatTran(2701)

# truyền vào sẽ in ra
DatTran(2701, "ILoveYou")


def f(Louis=[]):
	Louis.append("F")
	print(Louis)

f()
f()

def team(a, b):
	pass # lệnh giữ chỗ

team(18, "TechUni")

# thay đổi thứ tự truyền parameter
team(b="TechUni", a=18)

print(sorted([3, 4, 1], reverse=True))


def Teo(a, b=2, c=3, d=4):
	f = (a + d) * (b + c)
	print(f)

# pass argument theo keyword
Teo(1, d=5)


# * không được tính là keyword
# tất cả phía sau * đều là keyword argument
def example(pos_or_key_arg, *, key_arg1=1, key_arg2="BaoTran"):
	print(pos_or_key_arg)
	print(key_arg1)
	print(key_arg2)

example(1)

def example2(k, t, e, *, r="List"):
	print(k)
	print(t, e)
	print("end", r)

lst = ["123", "Dat", 69.96]
#example2(lst[0], lst[1], lst[2], lst[3])

# lấy giá trị tuần tự đưa vào
# có thể lấy từ các container khác như tuple, string, set
# riêng dict chỉ có thể lấy được key
example2(*lst, r="Hello")

def example3(*args):
	print(args)
	print(type(args))

example3('Dat', 27, "Tran") #tuple

example3(*(x for x in range(7))) #unpack xong pack


# phải đặt tên biến trùng với key mới có thể xuất ra value
def example4(Name, Member):
	print(Name)
	print(Member)

dic = {"Name": "Dat", "Member": 18}

example4(**dic) 


def example5(**kwargs):
	for key, value in kwargs.items():
		print(key, "=>", value)

example5(name="Tran", member=18)

# có thể khai báo biến trong hàm (LOCAL)
# biến khai báo ở hàm nào chỉ có hàm đó biết
# biến khai báo ở ngoài hàm có thể dùng trong hàm, ngược lại thì không
def say_slogan():
	Dat = "BaoTran"
	print("I love", Dat)

say_slogan()

num = 69
st = "DatDuong"
lst = [1, 2, 3]
tup = tuple("Education")

def change(parameter):
	parameter = "New Value"
	print("Changed successfully")

change(num)
change(st)
change(lst)
change(tup)
print("*" * 10)
print("{}\n{}\n{}\n{}\n".format(num, st, lst, tup))

lst_ = ["BaoTranne", 1, 2]

def change2(parameter):
	parameter[1] = "New Value"
	print("Changed successfully")

print(lst_)
change2(lst_)
print(lst_)


def make_slogan():
	# khởi tạo với global không có giá trị
	global slogan
	# sau khi khởi tạo xong, ta mới gán giá trị 
	slogan = "BaoTranCute"


make_slogan()

print(slogan)

def make_global():
	global x
	x = 1

def local():
	x = 5
	print("x in local", x)


make_global()
print(x)

local()
print(x)

# lưu ý: không nên dùng global trừ khi cần thiết
# nó sẽ làm cho chương trình rối hơn

def cal_rec_per(width, height):
	per = (width + height) * 2
	return per

rec_1_width = 5
rec_1_height = 3

# khởi tạo 1 biến để hứng kết quả
rec_1_per = cal_rec_per(rec_1_width, rec_1_height)

print(rec_1_per)

# trường hợp này là khi bạn không cần tái sử dụng
print(cal_rec_per(7, 4))



def _return_ter_func():
	print("Chúng ta sử dụng return để ngắt hàm")
	# dòng dưới đây tương tự như bạn viết return none
	return 
	print("Hàm print này dĩ nhiên không được gọi")

none = _return_ter_func()
print(type(none))


def cal_rec_area_per(width, height):
	perimeter = (width + height) * 2
	area = width * height
	return perimeter, area

rec_width = 3
rec_height = 9
rec_per, rec_area = cal_rec_area_per(rec_width, rec_height)

print(rec_per, rec_area)


Dat_lst = [1, "BaoTran", 2]
for value in Dat_lst:
	print(value)

Dat_gen = (value2 for value2 in range(3))
for value2 in Dat_gen:
	print(value2)


def square(Lst):
	for num in Lst:
		yield num**2


Dat_ret = square([1, 2, 3])
for value3 in Dat_ret:
	print(value3)


def gen():
	yield "Dat"
	print("This is the second yield")
	yield "Tran"
	print("This is the last yield")
	yield "Hello"
	print("Will not return anything")


for value4 in gen():
	print(value4)	


def gen2():
	while True:
		x = yield # yield None
		yield x ** 2	

g = gen2()
next(g)
print(g.send(2))
next(g)
print(g.send(10))



ave = lambda a, b, c: (a + b + c)/3
print(ave(1, 3, 2))

x_power_a = lambda x, a=2: x ** 2
print(x_power_a(2))


def Datteam():
	mem = lambda x: x + ' is a member of Kteam'
	return mem # trả về 1 hàm nặc danh

call_mem = Datteam() # lấy biến giữ hàm nặc danh
print(call_mem("Tran")) # giá trị chuỗi được đưa vào cho biến


Datlst = [lambda x: x**2, lambda x: x**3, lambda x: x**4]
print(Datlst[1](2))


for func in Datlst:
	print(func(3))


key = "Tran"
print({"Google": lambda: "Gooog",
"Youtube": lambda: "Youuuuu",
"Tran": lambda: "Beautiful"}[key]())


find_greater = lambda x, y: x if x > y else y
print(find_greater(6, 2))

# nếu x chia hết cho 2 và 3, sẽ trả ra 1, ngược lại là 0
cd_of_2_3 = lambda x: (1 if x % 3 == 0 else 0) if x % 2 == 0 else 0
print(cd_of_2_3(6))


def Tran(first_string):
	return lambda second_string: first_string + second_string

slogan = Tran("Datne") # gửi giá trị cho biến first_string
print(slogan("Lovely"))


def mymap(funct, iterable):
	for x in iterable:
		yield funct(x)

def inc(x): return x + 1

Tranteam1 = [1, 2, 3, 4]

# dùng constructor list để quan sát dữ liệu
print(list(map(inc, Tranteam1)))
print(list(map(lambda x: x + 1, Tranteam1)))

inc = lambda x: x + 1
print([inc(x) for x in Tranteam1])


# cộng tuần tự phần tử
funct_add = lambda x, y: x + y
Tranteam2 = [5, 6, 7, 8]
Tran = map(funct_add, Tranteam1, Tranteam2)
print(list(Tran))


lst_1 = [1, -3, 5, 0, 2, 6, -4, -9]
func_ = lambda x: x > 0 # điều kiện

# filter: lọc theo điều kiện
print(list(filter( func_, lst_1)))

print([x for x in lst_1 if x > 0])

# loại 0 ra khỏi list
print(list(filter(None, lst_1)))


from functools import reduce

# (((1+2)+3)+4)
print(reduce(funct_add, Tranteam1))

funct_multi = lambda x, y: x * y

# (((1+2)+3)+4) + 10
print(reduce(funct_add, Tranteam1, 10))

# (((1*2)*3)*4) * 10
print(reduce(funct_multi, Tranteam1, 10))

'''			đệ quy			'''

def cal_sum(lst_):
	if not lst_: # tương đương if len(lst_) == 0:
		return 0
	else:
		return lst_[0] + cal_sum(lst_[1:])

print(cal_sum([1, 2, 3, 4]))
print(cal_sum([1, 2, 3, 4, 5]))


def cal_sum1(lst_1):
	idx0, *r = lst_1
	return idx0 if not r else idx0 + cal_sum1(r)

print(cal_sum1([1, 2, 3]))
print(cal_sum1(["a", "b", "c"]))
print(cal_sum1([[1, 2], [3, 4], [5, 6]]))


def cal_sum2(lst_2):
	if not lst_2: return 0
	return call_cal_sum(lst_2)

def call_cal_sum(lst_2):
	return lst_2[0] + cal_sum2(lst_2[1:])

print(cal_sum2([1, 2, 3, 4, 5]))

