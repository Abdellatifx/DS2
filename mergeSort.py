import math

import Main
import time
import sys
sys.setrecursionlimit(10**7)


def merge(arr, left, right):
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i = i + 1
        else:
            arr[k] = right[j]
            j = j + 1
        k = k + 1
    while i < len(left):
        arr[k] = left[i]
        k = k + 1
        i = i + 1
    while j < len(right):
        arr[k] = right[j]
        k = k + 1
        j = j + 1
    return arr


def merge_sort(arr):
    first_time = time.time()
    if len(arr) > 1:
        middle = len(arr)//2
        left = arr[:middle]
        right = arr[middle:]
        merge_sort(left)
        merge_sort(right)
        arr = merge(arr, left, right)
    second_time = time.time()
    if len(arr) == 10 or len(arr) == 100 or len(arr) == 1000 or len(arr) == 10000 or len(arr) == 100000:
        print("The merge sorted array with size ", len(arr), "is ")
        for i in range(0, len(arr)):
            print("array[", i, "] = ", arr[i])
    return second_time - first_time
