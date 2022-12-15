# Viết hàm nhập từ bàn phím và hiển thị ra màn hình danh sách hai chiều kích thước MxN

def matrix(m, n):
    emptylist = []
    for i in range(m):
        inputlist = input("enter column {}: ".format(i+1)).split()
        if len(inputlist) != n:
            print("Invalid Input!")
            break
        else:
            emptylist.append(inputlist)
    return emptylist

def printlist(m, n):
    for j in matrix(m, n):
        print(max(j))
    
inputlist = input("Input m and n: ").split()

if len(inputlist) == 0:
    print("Empty Input!")
elif len(inputlist) != 2:
    print("Input must be equal 2!")
else:
    try: 
        m, n = map(int, inputlist)
        assert m > 0 or n > 0
        printlist(m, n)
    except AssertionError:
        print("m and n must greater than 0!")
    except ValueError:
        print("Invalid Input!")
