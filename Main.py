import selectionSort
import mergeSort
import random

arr = []
for i in range(1, 6):
    n = 10**i
    for j in range(0, n):
        arr.append(random.randrange(0, n, 1))
    selection_sort_time = selectionSort.selection_sort(arr, n)
    print(n)
    print(selection_sort_time)


