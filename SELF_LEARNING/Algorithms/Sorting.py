
data = [-2, 45, 0, 11, -9]

"""             Bubble Sorting              """

# Bubble sort is a sorting algorithm that compares two adjacent elements
# and swaps them until they are not in the intended order.

def BubbleSort(array):
    length = len(array)
    if length <= 1:
        return array
    else:
        for i in range(len(array)):
            for j in range(len(array) - i -1):
                if array[j] > array[j+1]:
                    temp = array[j]
                    array[j] = array[j+1]
                    array[j+1] = temp
        return array

print("Sorted Array in Ascending Order: ", *BubbleSort(data))

def OptimizedBubbleSort(array):
    length = len(array)
    if length <= 1:
        return array
    else:
        for i in range(len(array)):
            swapped = False
            for j in range(len(array) - i - 1):
                if array[j] > array[j+1]:
                    temp = array[j]
                    array[j] = array[j+1]
                    array[j+1] = temp
                    swapped = True
            if not swapped:
                break
        return array

print("Sorted Array in Ascending Order: ", *OptimizedBubbleSort(data))

"""             Selection Sorting              """

# Selection sort is a sorting algorithm that selects the smallest element from an unsorted list in each iteration
# and places that element at the beginning of the unsorted list.

def SelectionSort(array):
    length = len(array)
    if length <= 1:
        return array
    else:
        for step in range(len(data)):
            min_idx = step
            for i in range(step + 1, len(data)):
                if array[i] < array[min_idx]:
                    temp = array[i]
                    array[i] = array[min_idx]
                    array[min_idx] = temp
        return array

print("Sorted Array in Ascending Order: ", *SelectionSort(data))

"""             Insertion Sorting              """

# Insertion sort is a sorting algorithm that places an unsorted element at its suitable place in each iteration.

def IsertionSort(array):
    indexing_length = range(1, len(array))
    for i in indexing_length:
        value_to_sort = array[i]
        
        while array[i-1] > value_to_sort and i>0:
            array[i], array[i-1] = array[i-1], array[i]
            i = i - 1

    return array

print("Sorted Array in Ascending Order: ", *IsertionSort(data))

"""             Quick Sorting              """

# Quicksort is a sorting algorithm based on the divide and conquer approach

def QuickSort(array):
    length = len(array)
    if length <= 1:
        return array
    else:
        pivot = array.pop()

    items_greater = []
    items_lower = []

    for item in array:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)

    return QuickSort(items_lower) + [pivot] + QuickSort(items_greater)

print("Sorted Array in Ascending Order: ", *QuickSort(data))

