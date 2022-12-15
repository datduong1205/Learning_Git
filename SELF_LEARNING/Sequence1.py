''' 
Đây là chú thích đầu file py
Còn muốn ghi gì thì ghi vào đây
Đây là phần comment section
'''
	# phần 1
# in được nhiều dòng 1 lệnh
lover = '''Bao Tran
I love you so much babe
I wanna live with you forever'''
print(lover)
 
print("Duong\nLe\nMinh\nDat") # \n = xuống dòng

print('\a') # phát ra tiếng bíp
print('\b')	# đưa con trỏ chuột về 1 khoảng trắng		
print('\n')	# đưa con trỏ xuống dòng tiếp theo	
print('\t') # in ra 1 Horizontal Tab
print('\'')	# in ra ký tự '		
print('\\')	# in ra ký tự \

	# phần 2

# r trước chuỗi sẽ bỏ qua escape sequence
print(r'\neu mot ngay nao do')  

strA = 'Duong Le Minh Dat \n'
strB = '12A7 11'
strC = strA + "\n"  + strB
strD = strA * 5
print(strC)
print(strD)

# kiểm tra chuỗi có nằm trong chuỗi không
strE = strB in strA 
print(strE)

# đánh dấu thứ tự trong chuỗi bắt đầu từ 0
# khoảng cách (space) cũng tính là 1 đơn vị vị trí
# lấy ký tự nằm ở vị trí số 0 trong chuỗi A
strF = strA[len(strA) - 3] 
print(strF)

strG = strA[6:None] 
print(strG)

strH = strA[None:None:2]
print(strH)

# int: số nguyên
a = int("69") + 1
b = 69 + 1
print( str(a) + " + " + str(b) + " = " +str(a+b))

# float: số thực
c = float("6.9")
print(c)

print(str(27) + "01")

#replace chữ (rườm rà vcl)
d = strA[None:6] + "Tao " + strA[9:None]

print(hash(d))

