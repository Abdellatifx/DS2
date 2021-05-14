import matplotlib.pyplot as plt
import numpy as np


def plotting(a, x):
    for i in range(1, 4):
        x.append(10 ** i)
    plt.plot(x, a, color='r', label='insertion')
    plt.xlabel("Array size")
    plt.ylabel("Execution time")
    plt.legend
    plt.show()
