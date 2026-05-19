def bubbleSort(array):
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp


array = [42, 7, 15, 99, 3, 56, 28, 71, 14, 88, 5, 63, 37, 22, 50]

bubbleSort(array)
print(array)
