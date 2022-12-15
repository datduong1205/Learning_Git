# Viết hàm với tham số truyền vào là một danh sách các số thực. Sắp xếp danh sách theo thứ tự tăng dần (Không sử dụng hàm sắp xếp có sẵn).

isParseDone = False

def SelectionSort(array):
    length = len(array)
    if length <= 1:
        return array
    else:
        for step in range(len(array)):
            min_idx = step
            for i in range(step + 1, len(array)):
                if array[i] < array[min_idx]:
                    array[min_idx], array[i] = array[i], array[min_idx]
        return array

try:
    array = list(map(int, input("Sequence Number: ").split()))
    isParseDone = True
except ValueError:
    print("Invalid Input!")

if isParseDone:
    print("Sorted Array in Ascending Order: ", *SelectionSort(array))

    