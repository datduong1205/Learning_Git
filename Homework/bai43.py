# Viết hàm tính tổng các số với số lượng bất kỳ (Tham số là *agrs).

def sum(*args):
    result = 0
    for i in args:
        result += i
    return result
        

print("1 + 2 + 3 = {}".format(sum(1, 2 ,3)))
print("1 + 2 + 3 + 4 + 5 = {}".format(sum(1, 2, 3, 4, 5)))