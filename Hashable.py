a = id(5)
print(a)

n = 69
print(n) 
print(n + 1)

# .__add__: cộng 1 đơn vị
print(n.__add__(1))

# .__sub__: trừ 1 đơn vị
print(n.__sub__(1))

# .__mul__: nhân
print(n.__mul__(2))

# .__neg__(): thêm dấu trừ thành số âm
print(n.__neg__())

s1 = "HowKteam"
s2 = "Free education"

#s1 = s1 + "Python"
#s2 += "Python"

print(id(s1))
print(id(s2))

s3 = [1,2]
s4 = [3,4]

print(id(s3))
print(id(s4))

s3 = s3 + [0]
s4 += [0]

print(id(s3))
print(id(s4))

# +=
s3.__add__([3,4])
print(s3)


