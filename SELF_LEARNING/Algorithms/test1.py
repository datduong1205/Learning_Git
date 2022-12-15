def QuickSort(array):
    length = len(array)
    if length <= 1:
        return array
    else:
        pivot = array.pop()

    numberofcomparision = 0
    items_greater = []
    items_lower = []

    for item in array:
        numberofcomparision +=1
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)
    
    print(numberofcomparision)
    return QuickSort(items_lower) + [pivot] + QuickSort(items_greater)


data = [6, 5, 17, 15, 16, 20, 18, 7]
data2 = [15, 6, 5, 17, 16, 20, 18, 7]
QuickSort(data2)
