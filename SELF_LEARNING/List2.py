
# .count đếm số lần xuất hiện của 1 phần tử
a = [1,1,1,2,3,4,5,6,7,8,9]
b = a.count(1)
print(b)

# .index trả ra vị trí của phần tử nằm trong list
print(a.index(1))

# .copy sao chép phần tử
# tương đương với list()
c = a.copy()
c[0] = 'York'
print(a)
print(c)

# .clear xóa mọi phần tử có trong chuỗi
d = a.clear()
print(a)
print(d)

# .append cộng thêm phần tử vào chuỗi (đưa về cuối)
a.append([4,5])
print(a)

# .extend nhét từng phần tử vào, không tạo vòng lập
a.extend([6,7,[8,9]])
print(a)

# .insert thêm 1 phần tử nào vào 1 vị trí đã nhập (vị trí + phần tử)
a.insert(0,99)
print(a)

# .pop bỏ 1 phần tử theo vị trí đã cho trong chuỗi
# nếu không nhập, mặc định xóa phần tử cuối 
a.pop(1)
print(a)

# .remove xóa đi phần tử được nhập
a.remove([8,9])
print(a)

# .preverse đảo ngược list
a.reverse()
print(a)

# .sort sắp xếp mặc định từ nhỏ tới lớn
a.sort(key=None, reverse=True)
print(a)

