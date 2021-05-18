import array
import plotting
import bubbleSort
import heapSort
import insertionSort
import mergeSort
import quickSort
import selectionSort
import SortingFunc


def Type():
    rows, cols = (6, 5)
    arr = [[0] * cols] * rows
    array = [[0] * cols] * rows
    for i in range(0, 4):
        array[i] = SortingFunc.arraygeneration(10**(i+1))

    method = insertionSort
    arr[0] = SortingFunc.sorter(method, "Insertion", array)

    method = bubbleSort
    arr[1] = SortingFunc.sorter(method, "Bubble", array)

    method = selectionSort
    arr[2] = SortingFunc.sorter(method, "Selection", array)

    method = mergeSort
    arr[3] = SortingFunc.sorter(method, "Merge", array)

    method = heapSort
    arr[4] = SortingFunc.sorter(method, 'Heap', array)

   # method = quickSort
   # arr[5] = SortingFunc.sorter(method, "Quick", array)
    print(arr)
#    plotting.plotting(arr)
