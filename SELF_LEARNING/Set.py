# Set chỉ có thể chứa các Hashable Object 
# Set không là 1 Hash Object
# Không thể chứa 1 set trong 1 set
# Không thể chứa 1 list trong 1 set
# Không thể tạo 1 empty set

set1 = {69, 96}
print(set1)
print(type(set1))

set2 = {"Duong Le Minh Dat"}
print(set2)

set3 = {(69, "Tao Nguyen Bao Tran"), (1, 2, 3)}
print(set3)

# chỉ giữ lại 1 số 1
set4 = {1, 1, 1}
print(set4)

# dict
set5 = {}
print(type(set5))

set6 = {value for value in range(3)}
print(set6)

set7 = set((1, 2, 3))
print(set7)
print(type(set7))

set8 = set(("Duong Le Minh Dat"))
print(set8)
print(type(set8))

set9 = set(("aaaaaaaaaaaaa"))
print(set9)
print(type(set9))

set10 = set([1, 6, 8, 3, 1, 1, 3, 6])
print(set10)
print(type(set10))

set11 = set()
print(set11)
print(type(set11))

# Biểu đồ Venn

print(1 in {1, 2, 3})

# Không kiểm tra được 1 set nằm trong set
print({1, 2} in {1, 2, 3})

print((1, 2) in {(1, 2), 3})

print({1, 2, 3, 4} - {2, 3})

# in ra 1 set vừa tồn tại trong set 1 vừa tồn tại trong set 2
print({1, 2, 3, 4} & {4, 5}) # và

# lấy hết phần tử cả 2 bên đều có 
print({1, 2, 3, 4} | {4, 5}) # hoặc

# lấy hết tất cả phần tử 2 bên và loại đi phần tử trùng nhau
print({1, 2, 3, 4} ^ {4, 5}) # XOR


# Python không hỗ trợ index và cắt set

set10.clear()
print(set10)

# .pop: bóc phần tử đầu tiên ra khỏi set và loại bỏ nó
# set rỗng pop sẽ lỗi

set7.pop()
print(set7)

set7.remove(2)
print(set7)

# .discard: loại bỏ nhưng nếu không có trong set cũng không báo lỗi
set7.discard(6)
print(set7)

set12 = set7.copy()
print(set12)

set7.add(1)
print(set7)

