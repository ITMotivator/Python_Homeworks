# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. 
# m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

import random

length1 = int(input("Enter first list size "))
firstList = [random.randint(1, 10) for _ in range(length1)]
print(firstList)
set1 = set(firstList)

length2 = int(input("Enter second list size "))
secondList = [random.randint(1, 10) for _ in range(length2)]
print(secondList)
set2 = set(secondList)

result = sorted(set1.intersection(set2))
print(result)