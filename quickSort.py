import sys

import ParentClass

sys.setrecursionlimit(10**7)


def partition(array, start, end):
    pivot = start
    index = start + 1
    while True:
        while index <= end and array[end] >= pivot:
            end = end-1
        while index <= end and array[index] <= pivot:
            index = index+1
        if index <= end:
            array[index], array[end] = array[end], array[index]
        else:
            break
        array[index], array[start] = array[start], array[index]
    return pivot


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
