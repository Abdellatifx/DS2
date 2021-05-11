def insertion(array):
    for i in range(1, len(array)):
        key = array[i]
        hole = i
        while(hole > 0 and array[hole - 1] > key):
            array[hole] = array[hole - 1]
            hole = hole - 1
        array[hole] = key


arr = [12, 11, 13, 5, 6]
insertion(arr)
print("Sorted array is:")
for j in range(len(arr)):
    print("%d" % arr[j])
