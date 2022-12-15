# Viết hàm hiển thị ra màn hình câu sau: “Xin chao! Toi la {Ten}, toi {Tuoi} tuoi.”. Với tham số là {Ten} và {Tuoi}

isParseDone = False

def PersonalInfo(name, age):
    if age < 0:
        print("age must be greater than 0")
    else:
        print("Hello! My name is {}, I'm {} years old".format(name, age))

try:
    nameInp = input("Enter your name: ")
    ageInp = int(input("Enter your age: "))
    isParseDone = True
except ValueError:
    print("Invalid Input!")

if isParseDone:    
    PersonalInfo(nameInp, ageInp)

