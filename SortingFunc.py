import random
import time


def arraygeneration(size):
    arr = []
    for j in range(0, size):
        arr.append(random.randrange(0, 1000, 1))
    return arr


def printarray(arr, n, type):
    print("The", type, "sorted array with size ", n, "is ")
    for i in range(0, 3):
        print("array[", i, "] = ", arr[i])


def sorter(method, type):
    N = 6
    ar = [0] * N
    j = 0
    for i in range(1, 2):
        n = 10 ** i
        arr = arraygeneration(n)
        start_time = time.time()
        arr = method.sort(arr)
        end_time = time.time()
        ar[i-1] = (end_time - start_time)
        printarray(arr, n, type)
        print("Sorting time  for size", n, "is ", end_time - start_time)
    return ar
