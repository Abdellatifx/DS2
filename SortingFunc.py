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


def sorter(method):
    for i in range(1, 4):
        n = 10 ** i
        arr = arraygeneration(n)
        start_time = time.time()
        arr = method.sort(arr)
        end_time = time.time()
        printarray(arr, n, "Insertion")
        print("Insertion sort time for size", n, "is ", end_time - start_time)
