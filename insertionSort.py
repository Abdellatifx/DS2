import time
import Main

def insertion(array):
    start_time = time.time()
    for i in range(1, len(array)):
        key = array[i]
        hole = i
        while hole > 0 and array[hole - 1] > key:
            array[hole] = array[hole - 1]
            hole = hole - 1
        array[hole] = key
    end_time = time.time()
    print("The insertion sorted array with size ", len(array), "is ")
    for i in range(0, len(array)):
        print("Array [", i, "] = ", array[i])
    return end_time - start_time