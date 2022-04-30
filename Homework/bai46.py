# Viết hàm giải phương trình bậc nhất và phương trình bậc hai với tham số là các hệ số của phương trình.

import math

def menu():
    print("Please choose: \n1: Simple Equation \n2: Quadratic Equation")


def SimpleEquation(a, b):
    if a == 0:
        if b == 0:
            return "The equation has infinite solution"
        return "The equation has no solution"
    return "The equation has 1 solution: x = {}".format(-b/a)


def QuadraticEquation(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                return "The equation has infinite solution"
            else:
                return "The equation has no soluton"
        else:
            return "The equation has 1 solution: x = {}".format(-c/a)
    else:
        delta = b*b - 4*a*c
        if delta > 0:
            x1 = (-b + math.sqrt(delta)) / (2*a)
            x2 = (-b - math.sqrt(delta)) / (2*a)
            return "The equation has 2 distinguise solutions: \nx1 = {} \nx2 = {}".format(x1, x2)
        elif delta == 0:
            x = -b / (2*a)
            return "The equation has 2 same solutions: x1 = x2 = {}".format(x)
        else:
            return "The equation has no solution"
        

try:
    menu()
    type = int(input("Type in the kind of equation you want: "))
    if type == 1:
        a, b = map(float, input("Type in the coefficients: ").split())
        print(SimpleEquation(a, b))    
    elif type == 2:
        a, b, c = map(float, input("Type in the coefficients: ").split())
        print(QuadraticEquation(a, b, c))    
    else:
        menu()
except ValueError:
    print("Invalid Input!")


 