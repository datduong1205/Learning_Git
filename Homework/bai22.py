# Viết chương trình nhập vào từ file input ba số a, b, c. 
# Nếu a, b, c là ba cạnh của một tam giác thì kiểm tra và xuất ra file output thông báo loại của tam giác (Có xử lý ngoại lệ đầu vào).

try:
    with open("triangle.inp", mode="r", encoding="utf8") as Inputside:
        side = Inputside.readline().rstrip("\n")

    a, b, c = map(float, side.split())

    if a + b > c and a + c > b and b + c > a:
        if a*a == b*b + c*c or b*b == a*a + c*c or c*c == a*a + b*b:
            triangle = "Right Triangle"
        elif a == b == c:
            triangle = "Equilateral Triangle"
        elif a == b or a == c or b == c:
            triangle = "Isoceles Triangle"
        elif a*a > b*b + c*c or b*b > a*a + c*c or c*c > a*a + b*b:
            triangle = "Obtuse Triangle"
        else:
            triangle = "Pointed Triangle"
    else:
        triangle = "{}, {} and {} are not 3 sides of a triangle!".format(a, b, c)

    with open("triangle.out", mode="wb") as Outputresult:
        Outputresult.write(triangle.encode("utf8"))

    print("Done!")
    
except ValueError:
    print("Invalid Input!")
    Error = "Invalid Input"

except FileNotFoundError:
    print("File Doesnt Exist!")
    Error = "File Doesnt Exist!"

with open("triangle.out", mode="wb") as Outputresult:
    Outputresult.write(Error.encode("utf8"))

