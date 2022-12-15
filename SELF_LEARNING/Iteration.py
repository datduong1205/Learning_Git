# không thể truy xuất trực tiếp tới giá trị của Iterator
# phải truy xuất từng phần tử

# generator object
itera = (x for x in range(3))
print(itera)

print(next(itera))
print(next(itera))
print(next(itera))

#print(itera[0]) : không thể truy xuất trực tiếp tới index

# tổng từ 0-9 rồi + thêm 2
# sau khi sum con trỏ đã chỉ về cuối
itera2 = (x for x in range(10))
print(sum(itera2,2))

itera3 = (x for x in range(12))
print(max(itera3))

# nếu không có dữ liệu, sẽ trả default value
print(max([], default = "HelloBaoTran"))

print(max(9, 5, 21, 32, 2701))

print(min(21, 32, 4124))


print(sorted((1, 3, 2, 123, 42), reverse=True))


