# Viết hàm máy tính đơn giản cho hai số thực. Trong hàm có gọi 4 hàm con để tính các phép tính cộng, trừ, nhân, chia tương ứng.


# mỗi 1 hàm chỉ nên giữ 1 chức năng
def Plus(Num1, Num2):
    return Num1 + Num2

def Minus(MinusNum, Subtrahend):
    return MinusNum - Subtrahend

def Multi(Multiplier, Multiplicand):
    return Multiplier * Multiplicand

def Divide(Divisor, Dividend):
    return Divisor / Dividend

def Calculator(a, b, operator):
    if operator == "+":
        return Plus(a, b)
    elif operator == "-":
        return Minus(a, b)
    elif operator == "x":
        return Multi(a, b)
    elif operator == ":":
        return Divide(a, b)
    else:
        print("The operator must be: + - x :")

try:
    a, b = map(float, input("Type in 2 num: ").split())
    operator = input("Type in which operator you want: ")
    isParseDone = True 
    print("{} {} {} = {}".format(a, operator, b, Calculator(a, b, operator)))
except ValueError:
    print("Invalid Input!")
except ZeroDivisionError:
    print("ZeroDivisionError!")

    



