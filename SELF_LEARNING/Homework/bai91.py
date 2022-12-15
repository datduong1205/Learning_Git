# Viết hàm trả về danh sách hai chiều chuyển vị.  (Tham số là danh sách hai chiều MxN)

def InputList(M, N):
    twodimensionlist = []
    for i in range(M):
        row = input().split()
        if len(row) != N:
            print("two dimension list must be the same size!")
            return None
        twodimensionlist.append(row)
    return twodimensionlist

def PrintList(Matrix):
    for row in Matrix:
        print(*row)

def TransPoseList(Matrix):
    transposelist = []
    M = len(Matrix[0])
    N = len(Matrix)
    for i in range(M):
        column = [Matrix[j][i] for j in range[N]]
        transposelist.append(column)
    return transposelist

try:
    M, N = map(int, input("Input: ").split())
    if M <= 0, N <= 0:
        print("list length must be integer")
    else:
        Matrix = InputList(M, N)
        if Matrix is not None:
            TransPose_List = TransPoseList(Matrix) 
            PrintList(TransPose_List)
except ValueError:
    print("Invalid Input!")
