import time
import copy

palavras = list()

with open("loremipsum.txt", "r") as arquivo:
    for linha in arquivo:
        for palavra in linha.split():
            palavras.append(palavra)


def bubbleSort(array):
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp


def selectionSort(array):
    for i in range(len(array)):
        menor = i
        for j in range(i + 1, len(array)):
            if array[menor] > array[j]:
                menor = j
        array[i], array[menor] = array[menor], array[i]


lista_bubble = copy.copy(palavras)
inicio = time.time()
bubbleSort(lista_bubble)
fim = time.time()
print("Bubble Sort:", lista_bubble)
print("Tempo Bubble Sort:", fim - inicio)

lista_selection = copy.copy(palavras)
inicio = time.time()
selectionSort(lista_selection)
fim = time.time()
print("Selection Sort:", lista_selection)
print("Tempo Selection Sort:", fim - inicio)

lista_sort = copy.copy(palavras)
inicio = time.time()
lista_sort.sort()
fim = time.time()
print("Sort nativo:", lista_sort)
print("Tempo Sort nativo:", fim - inicio)

with open("palavras_ordenadas.txt", "w") as saida:
    for palavra in lista_sort:
        saida.write(palavra + "\n")
