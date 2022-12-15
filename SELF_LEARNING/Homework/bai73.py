# Viết hàm với tham số truyền vào là danh sách bất kỳ. Hiển thị các phần tử ra màn hình kèm với số thứ tự phía trước.

def inList(S):
    for num, value in enumerate(S):
        print(num, value)

S = input("Input: ").split()
inList(S)