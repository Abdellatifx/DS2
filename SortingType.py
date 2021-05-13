import bubbleSort
import heapSort
import insertionSort
import mergeSort
import quickSort
import selectionSort
from SortingFunc import sorter


def Type(num):
    if num == 1:
        method = insertionSort
        sorter(method)
    if num == 2:
        method = bubbleSort
        sorter(method)
    if num == 3:
        method = selectionSort
        sorter(method)
    if num == 4:
        method = mergeSort
        sorter(method)
    if num == 5:
        method = heapSort
        sorter(method)
    if num == 6:
        method = quickSort
        sorter(method)
