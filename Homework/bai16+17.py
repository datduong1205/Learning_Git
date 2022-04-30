# Viết chương trình nhập vào ba số a, b, c. Hiển thị ra màn hình cho biết a, b, c có là ba cạnh của một tam giác hay không.( có xử lý ngoại lệ)
# tổng 2 cạnh bất kỳ phải lớn hơn cạnh còn lại
isParseDone = False

try:
    a, b, c = map(float, input("Type in 3 sides of a triangle: ").split())
    isParseDone = True
except ValueError:
    print("Invalid Input!")

if isParseDone:
    if a <= 0 or b <= 0 or c <= 0:
        print("lenght must be larger than 0")
    else:
        if a + b > c and a + c > b and b + c > a:
            print("{}, {} and {} are 3 sides of a triangle".format(a,b,c))
        else:
            print("{}, {} and {} are not 3 sides of a triangle".format(a,b,c))
