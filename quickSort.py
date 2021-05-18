import sys

import ParentClass

sys.setrecursionlimit(100000000)


def partition(arr, start, end):
    i = (start - 1)
    pivot = arr[end]
    for j in range(start, end):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1


def quicksort(array, start, end):
    if start < end:
        pivot = partition(array, start, end)
        quicksort(array, start, pivot - 1)
        quicksort(array, pivot + 1, end)
    return array


def sort(array):
    start = 0
    end = len(array) - 1
    arr = quicksort(array, start, end)
    return  arr


class insert(ParentClass.SortMethods):
    pass
