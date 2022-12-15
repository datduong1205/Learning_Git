""" Viết chương trình nhập vào từ bàn phím một dãy số nguyên với độ dài bất kỳ, dãy số nằm trên 1 dòng,
các số cách nhau bởi khoảng trắng. Tính tổng của dãy số và hiển thị ra màn hình. """


daygiatri = input("Input:")

# sử dụng hàm split() để cắt giá trị thành các chuỗi
danhSachGiaTri = daygiatri.split()


try:
    # sử dụng hàm map() để thực hiện việc chuyển các chuỗi con sang kiểu số nguyên
    danhSachSo = map(int, danhSachGiaTri)
    tongDaySo = sum(danhSachSo)
    print(tongDaySo)
except ValueError:
    print("Invalid Input!")


