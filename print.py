print("DatDuong", "BaoTran", "YeuDau")

print("Hello", 69)

print(123, [4, 5, 6], "TranTao")

print("Anh", "Yeu", "Em", sep="-")

# end: không xuống dòng
print("Line 1", end="|||")
print("Line 2", end=" ")
print("Line 3")

# nhập hàm sleep từ thư viện time
from time import sleep 

print("start....", end='')
sleep(0.1) # dừng chương trình trong 3s
print("end...")

print("line 1\n", "line 2", end="")
sleep(0.1)
print("end...")


with open("employee.txt", "a") as f:
	print("Printed by print function", file=f)


# flush : mặc định là FALSE
# flush yêu cầu bộ đệm xuất ra những gì có trong bộ đệm
print("start...", end='', flush=True)
sleep(0.1)
print("end...")

your_name = "BaoTran"
your_great = "Hello! My name is "

for c in your_great+your_name:
	print(c, end="", flush=True)
	sleep(0.1)
print()

