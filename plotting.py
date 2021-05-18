import matplotlib.pyplot as plt


def plotting(array):
    size = [10, 100, 1000, 10000, 10001]
    plt.plot(size, array[0], color='r', label='insertion')
    plt.plot(size, array[1], color='b', label='bubble')
    plt.plot(size, array[2], color='g', label='selection')
    plt.plot(size, array[3], color='c', label='merge')
    plt.plot(size, array[4], color='k', label='heap')
    plt.plot(size, array[5], color='y', label='quicksort')
    plt.xlabel("Array size")
    plt.ylabel("Execution time (in seconds)")
    plt.grid()
    plt.legend()
    plt.ylim(top=1, bottom=0)
    plt.show()
