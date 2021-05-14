import array

import bubbleSort
import heapSort
import insertionSort
import mergeSort
import quickSort
import selectionSort
from SortingFunc import sorter


def Type():
    rows, cols = (6, 6)
    arr = [[0] * cols] * rows

    method = insertionSort
    arr[0] = sorter(method, "Insertion")

    method = bubbleSort
    arr[1] = sorter(method, "Bubble")

    method = selectionSort
    arr[2] = sorter(method, "Selection")

    method = mergeSort
    arr[3] = sorter(method, "Merge")

    method = heapSort
    arr[4] = sorter(method, 'Heap')

    #method = quickSort
   # arr[5] = sorter(method, "Quick")
    print(arr)
