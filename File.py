
file_object = open("employee.txt", mode="r+")
print((file_object))
print(type(file_object))

data = file_object.read()
print(data)

# kết quả không in ra gì, vì con trỏ đang nằm ở cuối file
data2 = file_object.read(5)
print(data2)

file_object.close()

# .read(): truyền 1 con số vào, file sẽ được đọc tới vị trí đã truyền
# nếu không truyền, mặc định sẽ đọc hết file
file_object = open("employee.txt", mode="r+")

data3 = file_object.read(10)
data4 = file_object.read(20)
file_object.close()

print(data3)
print(data4)

file_object = open("employee.txt", "r+")

# .readline(): đọc từng dòng
data5 = file_object.readline()

file_object.close()

print(data5)

file_object = open("employee.txt", "r+")

# readlines(): đọc toàn bộ file và bỏ hết vào list
# với các phần tử trong list là mỗi dòng của file
data6 = file_object.readlines()

file_object.close()

print(data6)

file_object = open("employee.txt", "r+")

data7 = list(file_object)

file_object.close()

print(data7)

file_object = open("employee.txt", "a+")

data8 = file_object.write("\nBaoTranYeuDauZTa")

file_object.close()

print(data8)

file_object = open("employee.txt", "r")

data9 = file_object.read()

print(data9)

# đưa con trỏ về vị trí đầu
file_object.seek(0)

data10 = file_object.read()

print(data10)

file_object.close()









