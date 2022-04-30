# Viết chương trình giải phương trình bậc nhất và phương trình bậc hai
#  với các hệ số được nhập từ file input và kết quả được xuất ra file output (Có xử lý ngoại lệ đầu vào)

import math

try:
    with open("equation.inp", mode="r", encoding="utf8") as Mainfile:
        choice = int(Mainfile.readline())
        coefficents = Mainfile.readline().rstrip("\n")

    if choice == 1:
        print("Simple Equation ")
        a, b = map(float, coefficents.split())
        if a == 0:
            if b == 0:
                equation = "Infinite Solutions"
            else:
                equation = "No Solution"
        else:
            equation = "The equation has 1 solution: x= {} ".format(-b/a)

    elif choice == 2:
        a, b, c = map(float, coefficents.split())
        print("Quadratic Equation ")
        if a == 0:
            if b == 0:
                if c == 0:
                    equation = "Infinite Solution"
                else:
                    equation = "No Solution"
            else:
                equation = "The Equation has 1 solution: x= {} ".format(-c/b)
        else:
            delta = b*b - 4*a*c
            if delta < 0:
                equation = "No Solution"
            elif delta == 0:
                x = -b / (2*a)
                equation = "The Equation has 2 same solutions: x1 = x2 = {} ".format(x)
            elif delta > 0:
                x1 = float(-b - math.sqrt(delta)/(2*a))
                x2 = float(-b + math.sqrt(delta)/(2*a))
                equation = "The Equation has 2 distinc solutions: x1 = {}, x2 = {} ".format(x1, x2)
    else:
        print("Please Only Enter 1 or 2")    
        equation = "Please Only Enter 1 or 2."

except ValueError:
    equation = "Invalid Error!"

except FileNotFoundError:
    equation = "File Doesnt Exist!"


with open("equation.out", mode="wb") as Final:
    Final.write(equation.encode("utf8"))





