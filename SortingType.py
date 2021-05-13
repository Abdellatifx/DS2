
import bubbleSort
import insertionSort
from SortingFunc import sorter


def Type(num):
    if num == 1:
        method = insertionSort
        sorter(method)
    if num == 2:
        method = bubbleSort
        sorter(method)
