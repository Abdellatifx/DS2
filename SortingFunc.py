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


def sorter(method, type):
    N = 5
    ar = [0] * N
    j = 0

    n = []
    for i in range(1, 5):
        n.append(10 ** i)
        arr = arraygeneration(n[i - 1])
    for i in range(1, 5):
        n = 10 ** i
        arr = arraygeneration(n)
        start_time = time.time()
        arr = method.sort(arr)
        end_time = time.time()
        ar[i - 1] = (end_time - start_time)
        printarray(arr, n[i - 1], type)
        # print("Sorting time  for size", n[i-1], "is ", end_time - start_time)
        printarray(arr, n, type)
        # print("Sorting time  for size", n, "is ", end_time - start_time)
    return ar
