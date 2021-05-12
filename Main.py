import selectionSort
import mergeSort
import quickSort
import insertionSort
import bubbleSort
import heapSort
import random
import time

for i in range(1, 3):
    arr = []
    n = 10 ** i
    for j in range(0, n):
        arr.append(random.randrange(0, 1000, 1))
    selection_sort_time = selectionSort.selection_sort(arr, n)
    print("Selection sort time for size", n, "is ", selection_sort_time)
    arr.clear()
    for j in range(0, n):
        arr.append(random.randrange(0, 1000, 1))
    start_time = time.time()
    arr = mergeSort.merge_sort(arr)
    end_time = time.time()
    print("The merge sorted array with size ", len(arr), "is ")
    for i in range(0, len(arr)):
        print("array[", i, "] = ", arr[i])
    print("merge sort time for size", n, "is ", end_time - start_time)
    arr.clear()
    for j in range(0, n):
        arr.append(random.randrange(0, 1000, 1))
    insertion_sort_time = insertionSort.insertion(arr)
    print("Insertion sort time for size", n, "is ", insertion_sort_time)
    arr.clear()
    for j in range(0, n):
        arr.append(random.randrange(0, 1000, 1))
    start_time = time.time()
    array = quickSort.quicksort(arr, 0, len(arr) - 1)
    print("The quick sorted array with size ", len(array), "is ")
    for i in range(0, len(array)):
        print("array[", i, "] = ", array[i])
    end_time = time.time()
    quick_sort_time = end_time - start_time
    print("Quick sort time for size", n, "is ", quick_sort_time)

    arr.clear()
    for j in range(0, n):
        arr.append(random.randrange(0, 1000, 1))
    start_time = time.time()
    array = bubbleSort.bubbleSort(arr)
    print("The bubble sorted array with size ", len(array), "is ")
    for i in range(0, len(array)):
        print("array[", i, "] = ", array[i])
    end_time = time.time()
    bubble_sort_time = end_time - start_time
    print("Bubble sort time for size", n, "is ", bubble_sort_time)

    arr.clear()
    for j in range(0, n):
        arr.append(random.randrange(0, 1000, 1))
    start_time = time.time()
    array = heapSort.heapSort(arr)
    print("The Heap sorted array with size ", len(array), "is ")
    for i in range(0, len(array)):
        print("array[", i, "] = ", array[i])
    end_time = time.time()
    heap_sort_time = end_time - start_time
    print("Heap sort time for size", n, "is ", heap_sort_time)
