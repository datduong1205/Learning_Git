'''			 phần 1			 '''
length = 3
iter_ = (x for x in range(length)) #0, 1, 2
c = 0

while 1:
	try:
		print(next(iter_))
	except StopIteration:
		break

h = (1, 2, 3)
print(type(h))

h, k, t = (1, 2, 3) # unpacking

print(h)
print(k)
print(t)

Iter_ = (x for x in range(3))

for value in Iter_:
	print("->", value)

DatDuong = {"12052004": "Le", "Bao": "Tran"}
list_values = list(DatDuong.items())

print(list_values)
print(list_values[0])
print(list_values[1])

for key, value in DatDuong.items():
	print(key, "=>", value)
	if (key == "Bao"):
		break

s = "Bao Tran"

for ch in s:
	if ch == " ":
		break
	else:
		print(ch)


for k in (1, 2, 3):
	print(k)
	if k % 2 ==0:
		break # bỏ qua else
else:
	print("Done!")


for f in (1, 2, 3):
	print(f)
	if f % 2 ==0:
		continue
else:
	print("Done!")


'''			 phần 2			 '''	

a = range(5) # 0, 1, 2, 3, 4
print(type(a))

print(a[2]) # có hỗ trợ indexing


# start, stop, step
print(list(range(2, 5))) 

print(list(range(4, 1, -1)))

print(list(range(2, -3, -1)))

print(2 in a)

lst = [5, (1, 2, 3), {"abc", "xyz"}]

for i in range(len(lst)):
	print(lst[i])
	i += 1

lst_ = [1, 2, 3]
for value in range(len(lst_)):
	lst_[value] += 1
print(lst_)

student_list = ["Tony", "Stark", "Thor", "Wonder"]

for student in student_list:
	print(student)

gen = (enumerate(student_list))
print(type(gen))

print(list(gen))

for idx, dat in enumerate(student_list, 5):
	print(idx, "=>", dat)