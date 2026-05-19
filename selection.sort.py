array = [42, 7, 15, 99, 3, 56, 28, 71, 14, 88, 5, 63, 37, 22, 50]

for i in range(len(array)):
    menor = i
    for j in range(i + 1, len(array)):
        if array[menor] > array[j]:
            menor = j
    array[i], array[menor] = array[menor], array[i]

print(array)
