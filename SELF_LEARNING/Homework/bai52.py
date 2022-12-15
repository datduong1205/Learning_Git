# Viết hàm truyền vào tham số là hai chuỗi s1 và s2. Trả về chuỗi kết quả bằng cách nối 2 chuỗi s1 và s2
#  sau khi được xử lý như sau: nếu độ dài chuỗi nào nhỏ hơn 5 thì lặp lại chuỗi đó 3 lần.

def String(a, b):
    if len(a) <= 5:
        a = a * 3
    if len(b) <= 5:
        b = b * 3 
    
    # cach 1   
    print("".join([a, b]))  
    # cach 2
    print(a+b)

a = input("Input: ")
b = input("Input: ")

String(a, b)
    

    