import math


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
    if len(arr) > 1:
        middle = len(arr)//2
        left = arr[:middle]
        right = arr[middle:]
        merge_sort(left)
        merge_sort(right)
        arr = merge(arr, left, right)
    return arr
