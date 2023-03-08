# Определить индексы элементов массива (списка), значения которых принадлежат
# заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

array = [random.randint(-10, 10) for _ in range(20)]
print(array)
rangeStart = int(input("Enter range start number "))
rangeEnd = int(input("Enter range end number "))
iArray = []
for i in range(20):
    if array[i] >= rangeStart and array[i] <= rangeEnd:
        iArray.append(i)
print(iArray)
