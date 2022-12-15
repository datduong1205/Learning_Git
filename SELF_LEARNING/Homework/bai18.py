# Viết chương trình nhập vào từ bàn phím một dãy số nguyên với độ dài bất kỳ, dãy số nằm trên 1 dòng, các số cách nhau bởi khoảng trắng.
# Tính tổng của dãy số và hiển thị ra màn hình (Có xử lý ngoại lệ đầu vào).



try:
    Firstnum, Secondnum = map(float, input("type in 2 random number:").split())
    operation = input("Type in which operations you want:")
    
    if operation == "Plus":
         print("{} + {} = ".format(Firstnum,Secondnum), Firstnum + Secondnum)

    elif operation == "Minus":
         print("{} - {} = ".format(Firstnum,Secondnum), Firstnum - Secondnum)

    elif operation == "Multi":
         print("{} * {} = ".format(Firstnum,Secondnum), Firstnum * Secondnum)

    elif operation == "Divide":
         print("{} / {} = ".format(Firstnum,Secondnum), Firstnum / Secondnum)
         
    else:
        print("Operation Not Exist!")
except ValueError:
    print("Invalid Input!")
except ZeroDivisionError:
    print("Cant divide by Zero")


