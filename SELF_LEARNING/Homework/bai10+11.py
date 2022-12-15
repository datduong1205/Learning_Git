'''Viết chương trình nhập vào từ file input {Tên}, {Tuổi hiện tại}
 và xuất ra file output theo mẫu sau: “Vao 20 nam nua, tuoi cua {Tên} se la {Tuổi cần tìm}”. (Có xử lý định dạng đầu vào). '''

try:
    with open("input.inp", mode="r", encoding="utf8") as fileInp:
        ten = fileInp.readline().rstrip("\n")
        tuoiHienTai = int(fileInp.readline().rstrip("\n"))

    with open("output.out", mode="wb") as fileOut:
        string = "20 năm nữa, tuổi của {} sẽ là: {}".format(ten, tuoiHienTai + 20)
        fileOut.write(string.encode("utf8"))
    
    print("Done!")

except FileNotFoundError:
    print("File Not Found!")
    with open("output.out", mode="w") as fileError:
        fileError.write("File Not Found!")

except ValueError:
    print("Invalid Input!")
    with open("output.out", mode="w") as inputError:
        inputError.write("Invalid Input!")



 