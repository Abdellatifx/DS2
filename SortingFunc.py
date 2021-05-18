import random
import time
import plotting


def arraygeneration(size):
    arr = []
    for j in range(0, size):
        arr.append(random.randrange(0, 10000, 1))
    return arr


def printarray(arr, n, type):
    print("The", type, "sorted array with size ", n, "is ")
    for i in range(0, n):
        print("array[", i, "] = ", arr[i])


def sorter(method, type, array):
    N = 5
    ar = [0] * N
    for i in range(1, 6):
        start_time = time.time()
        array[i] = method.sort(array[i])
        end_time = time.time()
        ar[i-1] = (end_time - start_time)
        printarray(array[i], len(array[i]), type)
        print(type, "Sorting time  for size", len(array[i]), "is ", end_time - start_time)
    return ar
