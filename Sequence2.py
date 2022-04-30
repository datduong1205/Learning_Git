	# Phần 3
a = 'Bao Tran is my %s for almost %s year' %('LOVER','1')
print(a)

b = '%s %s'
result = b %('1','2')
print(result)

c = '%.3f' %(3.49999)
print(c)

d = f'Duong Le Minh Dat - York University'
print(d)

print(f'a\tb')

Name = 'Duong Le Minh Dat'
Address = ' 11 street 1 ward 10 Tan Binh distric'
Phone = '0855210070'
# f dùng để thay thế 
result1 = f'Student: {Name}\nAddress: {Address}\nPhone: {{Phone}}\n'
print(result1)

print('a: {}\nb: {}\nc: {}'.format(1,2,3))
# đánh STT vào ngoặc nhọn để đổi thứ tự truyền vào (start from 0)
print('d: {2}, b: {1}, c: {0}'.format(1,2,3))

# có thể gán biến
e = '1: {one}, 2: {two}, 3: {three}'.format(one=111, two=222, three=333)
print(e)

print('Duong {:^10} Le Minh'.format('Dat'))

row_1 = '+ {:-<6} + {:-^15} + {:->10} +'.format('', '', '')
row_2 = '| {:<6} | {:^15} | {:>10} |'.format('ID', 'Name', 'Noi sinh')
row_3 = '| {:<6} | {:^15} | {:>10} |'.format('1205', 'Louis Duong', 'Canada')
row_4 = '| {:<6} | {:^15} | {:>10} |'.format('2105', 'May Tao', 'Vietnam')
row_5 = '+ {:-<6} + {:-^15} + {:->10} +'.format('', '', '')
# Phần xuất kết quả
print(f'{row_1}\n{row_2}\n{row_3}\n{row_4}\n{row_5}')

	#  Phần 4

f = '12'
# mặc dù đã ép biến sang int nhưng căn bản vẫn là str 
print(int(f))
print(type(f))

g = 'york university'
# .captialize chỉ viết hoa chữ cái đầu tiên
h = g.capitalize()
print(h)

# .upper viết hoa tất cả chữ cái
i = g.upper()
print(i)

# .lower viết thường tất cả chữ cái
j = g.lower()
print(j)

# .swapcase viết thường -> viết hoa / viết hoa -> viết thường
k = g.swapcase()
print(k)

#  .title viết hoa chữ cái đầu của từng chữ
print(g.title())

# .center căn giữa cấu trúc: (khoảng cách, fill 'tối đa 1 ký tự')
print(g.center(50,'-'))

# .ljust căn trái
print(g.ljust(20, '-'))

# .rjust căn phải
print(g.rjust(20, '-'))

# encode = mã hóa
l = g.encode(encoding = 'utf-8', errors = 'strict')
print(l)

# kết quả: '1york university2york university3'
print(g.join(['1', '2', '3']))

# thay thế cái gì thành cái gì
# replace('', '', *count* 1 con số: replace bao nhiêu lần)
print(g.replace('university', 'college',))

# cắt chữ nào đó nằm ở 2 đầu 
print(g.strip('y'))

# cắt chữ ở bên trái / cắt chữ ở bên phải  
print(g.lstrip('y'))
print(g.rstrip('y'))

