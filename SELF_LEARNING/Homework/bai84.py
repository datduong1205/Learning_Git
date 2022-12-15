# Viết hàm với tham số truyền vào là hai danh sách cùng kích thước: danh sách tên và danh sách quốc tịch.
# Hiển thị ra màn hình tên và quốc tịch tương ứng với vị trí trong danh sách.

isParseDone = False

def delete_excessivespace(s):
    s = s.strip()
    while "  " in s:
        s = s.replace("  ", " ")
    return s

def name_nationality(namelist, nationalitylist):
    namelist = [delete_excessivespace(name) for name in namelist]
    nationalitylist = [delete_excessivespace(nationality) for nationality in nationalitylist]
    for name, nationality in zip(namelist, nationalitylist):
        print(name + " - " + nationality)

try:
    name = input("Name: ").split(",")
    nationality = input("Nationality: ").split(",")
    isParseDone = True
except ValueError:
    print("Invalid Input!")

if isParseDone:
    if len(name) == len(nationality):
        name_nationality(name, nationality)
    else:
        print("Name len must be equal to nationality len!")