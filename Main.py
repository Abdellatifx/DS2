import SortingType

while True:
    Method = int(input(
        "Select the sorting algorithm \n 1.Insertion Sort\n 2.Bubble Sort\n 3.Selection Sort \n 4.Merge Sort \n 5.Heap "
        "Sort\n 6.Quick Sort\n 7.Exit\n"))
    if Method == 7:
        exit(0)
    SortingType.Type(Method)
