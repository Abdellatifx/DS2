import SortingType
import selectionSort
import mergeSort
import quickSort
import insertionSort
import bubbleSort
import heapSort
import random
import time

Method = int(input(
    "Select the sorting algorithm \n 1.Insertion Sort\n 2.Bubble Sort\n 3.Selection Sort \n 4.Merge Sort \n 5.Heap "
    "Sort\n 6.Quick Sort\n"))
SortingType.Type(Method)

