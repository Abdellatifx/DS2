import selectionSort
import mergeSort
import random


for i in range(1, 5):
    arr = []
    n = 10**i
    for j in range(0, n):
        arr.append(random.randrange(0, n, 1))
    selection_sort_time = selectionSort.selection_sort(arr, n)
    print("Selection sort time for size", n, "is ", selection_sort_time)
    merge_sort_time = mergeSort.merge_sort(arr)
    print("merge sort time for size", n, "is ", merge_sort_time)
