import matplotlib.pyplot as plt
import numpy as np


def plotting(a, b, c, d, e, f, x):
    for i in range(1, 4):
        x = 10 ** i
    plt.plot(x, a, color='r', label='insertion')
    plt.plot(x, b, color='b', label='bubble')
    plt.plot(x, c, color='g', label='selection')
    plt.plot(x, d, color='y', label='merge')
    plt.plot(x, e, color='k', label='heap')
    plt.plot(x, f, color='m', label='quicksort')
    plt.xlabel("Array size")
    plt.ylabel("Execution time")
    plt.legend
    plt.show()
