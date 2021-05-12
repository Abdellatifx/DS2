import time


def selection_sort(arr, n):
    first_time = time.time()
    for i in range(0, n - 1):
        min_element = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_element] or arr[j] == arr[min_element]:
                min_element = j
        arr[i], arr[min_element] = arr[min_element], arr[i]
    second_time = time.time()
    print("The selection sorted array with size ", n, "is ")
    for i in range(0, n):
        print("array[", i, "] = ", arr[i])
    return second_time - first_time
