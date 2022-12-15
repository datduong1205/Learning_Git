# Viết chương trình nhập vào ba số a, b, c. Nếu a, b, c là ba cạnh của một tam giác thì kiểm tra và hiển thị ra màn hình loại của tam giác.

''' Algorithm:
Ba cạnh a, b, c của một tam giác phải thỏa mãn điều kiện là tổng hai cạnh bất kỳ luôn lớn hơn cạnh còn lại. Tức là a+b>c và a+c>b và b+c>a.
Tam giác vuông là tam giác có bình phương một cạnh bằng tổng bình phương hai cạnh còn lại. Ta kiểm tra điều kiện: a*a==b*b+c*c hoặc b*b==a*a+c*c hoặc c*c== a*a+b*b
Tam giác đều là tam giác có ba cạnh bằng nhau. Ta kiểm tra điều kiện a==b và b==c
Tam giác cân là tam giác có hai cạnh bằng nhau. Ta kiểm tra điều kiện: a==b hoặc a==c hoặc b==c
Tam giác tù là tam giác có một góc lớn hơn 90 độ. Từ điều kiện kiểm tra tam giác vuông, ta suy ra điều kiện để là tam giác tù là: a*a>b*b+c*c hoặc b*b>a*a+c*c hoặc c*c >a*a+b*b
Trường hợp còn lại sẽ là tam giác nhọn.
Dùng hàm print() để xuất thông báo theo yêu cầu.
'''


isParseDone = False

try:
    a, b, c = map(float, input("Type in 3 sides of a triangle: ").split())
    isParseDone = True
except ValueError:
    print("Invalid Error!")

if isParseDone:
    if a + b > c and a + c > b and b + c > a:
        if a*a == b*b + c*c or b*b == a*a + c*c or c*c == b*b + a*a:
            print("Right Triangle")
        elif a == b == c:
            print("Equilateral Triangle")
        elif a == b or a == c or b == c:
            print("Isosceles Triangle")
        elif a*a > b*b + c*c or b*b > a*a + c*c or c*c > a*a + b*b:
            print("Obtuse Triangle")
        else:
            print("Pointed Triangle")
    else:
        print("{}, {} and {} are not 3 sides of a triangle!".format(a, b, c))

