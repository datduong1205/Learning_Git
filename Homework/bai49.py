# Viết hàm đệ quy tính só fibonacci thứ n

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)
    
try:
    n = int(input("Type in 1 num: "))
    if n > 0:
        print(fibonacci(n))
    else:
        print("n must be greater than 0")
except ValueError:
    print("Invalid Input!")
