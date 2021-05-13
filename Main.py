import selectionSort
import mergeSort
import quickSort
import insertionSort
import bubbleSort
import heapSort
import random
import time


def arraygeneration(size):
    arr = []
    for j in range(0, size):
        arr.append(random.randrange(0, 1000, 1))
    return arr


def printarray(arr, n, type):
    print("The", type, "sorted array with size ", n, "is ")
    for i in range(0, n):
        print("array[", i, "] = ", arr[i])


for i in range(1, 2):
    n = 10 ** i

    arr = arraygeneration(n)
    start_time = time.time()
    arr = selectionSort.selection_sort(arr, n)
    end_time = time.time()
    printarray(arr, n, "Selection")
    print("Selection sort time for size", n, "is ", end_time - start_time)

    arr = arraygeneration(n)
    start_time = time.time()
    arr = mergeSort.merge_sort(arr)
    end_time = time.time()
    printarray(arr, n, "Merge")
    print("merge sort time for size", n, "is ", end_time - start_time)

    arr = arraygeneration(n)
    start_time = time.time()
    arr = insertionSort.insertion(arr)
    end_time = time.time()
    printarray(arr, n, "Insertion")
    print("Insertion sort time for size", n, "is ", end_time - start_time)

    arr = arraygeneration(n)
    start_time = time.time()
    array = quickSort.quicksort(arr, 0, len(arr) - 1)
    end_time = time.time()
    printarray(array, n, "Quick")
    print("Quick sort time for size", n, "is ", end_time - start_time)

    arr = arraygeneration(n)
    start_time = time.time()
    array = bubbleSort.bubblesort(arr)
    end_time = time.time()
    printarray(array, n, "Bubble")
    print("Bubble sort time for size", n, "is ", end_time - start_time)

    arr = arraygeneration(n)
    start_time = time.time()
    array = heapSort.heapsort(arr)
    end_time = time.time()
    printarray(array, n, "Heap")
    print("Heap sort time for size", n, "is ", end_time - start_time)
