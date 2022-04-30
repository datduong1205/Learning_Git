k = 5
while k > 0:
	print("k =", k)
	k -= 1

s = "DatDuong"
idx = 0
length = len(s)

while idx < length:
	print(idx, "stands for", s[idx])
	idx += 1

five_even_numbers = []
number = 1

while True:
	if number % 2 == 0:
		five_even_numbers.append(number)
		if len(five_even_numbers) == 5:
			break
	number += 1
print(five_even_numbers)
print(number)


Number = 1

while Number < 10:
	if Number % 2 == 0:
		Number += 1
		continue
	print(Number, "is an odd number")
	Number += 1

print(Number)

k = 0

while k < 3:
	print("Value of k is", k)
	k += 1
	if k == 2:
		break
else:
	print("k is not less than 3 anymore")

