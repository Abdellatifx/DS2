import time
from numpy import random
import sys


sys.setrecursionlimit(100000000)


def insertion(array):
    for i in range(1, len(array)):
        key = array[i]
        hole = i
        while hole > 0 and array[hole - 1] > key:
            array[hole] = array[hole - 1]
            hole = hole - 1
        array[hole] = key


def partition(array, start, end):
    pivot = start
    index = start+1
    while index <= end:
        if array[index] < array[start]:
            array[index], array[pivot] = array[pivot], array[index]
        index += 1
    array[pivot], array[start] = array[start], array[pivot]
    return pivot


def quicksort(array, start, end):
    if start < end:
        pivot = partition(array, start, end)
        quicksort(array, start, pivot - 1)
        quicksort(array, pivot+1, end)


arr = random.randint(1000, size=(10000))
start_time = time.time()
quicksort(arr, 0, len(arr)-1)
print("%s seconds" %(time.time()-start_time))
print("Sorted array is:")
for j in range(len(arr)):
    print("%d" % arr[j])
