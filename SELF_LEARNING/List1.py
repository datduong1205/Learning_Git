# 1 biến không thể lưu nhiều dữ liệu (bất lợi)
A = 'Tran'
print(A)
A = 18
print(A)

'''			list		'''
# list là danh sách 1 chiều
# được giới hạn bởi cặp ngoặc []
# các phần tử của list được cách nhau bởi dấu phẩy
# có khả năng chứa mọi giá trị của python, bao gồm cả chính nó

a = [1,2,3,"Duong Le Minh Dat",[[4,5,6,],["York"],["University"]]]
print(a)

# list rỗng
b = []

	# list comprehension
# hiểu là: cho biến có giá trị trong phạm vi từ [0,20) 
c = [age for age in range(20)]
print(c)

d = [[n, n*1, n*2] for n in range(1,4)]
print('\n' + str(d))

print([n*5 for n in range(1,5)])

	# constructor list
# iterable: dạng cấu trúc tổng hợp (int không phải tập hợp nhiều phần tử)
e = list('Duong Le Minh Dat')
print(e)

# 1 chuỗi không thể cộng với 1 list
f = [1,2]
f+= ['one', 'two'] # (f+=) tương đương (f = f +)

# chỉ có thể nhân số lượng list lên
# không thể nhân list với 1 chuỗi
f *=2
print(f)

g = 'York' in f 
print(g)

B = [[[1,2,3],[4,5,6]],'a','b','c',7,8,9]

print(B[0][1][2])

print(B[-1])

print(B[0:3])

print(B[None:2])

print(B[::-1])
# phần tử ở vị trí 1 đã bị thay đổi 
B[1] = 'York University'
h = B[1]
print(h)
print(B) # kết quả

'''			matrix		'''
# matrix là cấu trúc dữ liệu 2 chiều
# Ex: Excel bản chất là 1 ma trận

print(B[0][1])
print(B[1][5:None])
print(B[2])

# lưu ý: không được phép gán list này sang list kia nếu không có chủ đích
C = list(a) # sử dụng list constructor: clone C thành 1 list mới
print(C)
print(a)
C[0] = 'York'
print(C)
print(a)

D = list(a)
print('\n' + str(a))
print(D)
D[4] = 'Dat'

print('\n' + str(a))
print(D)