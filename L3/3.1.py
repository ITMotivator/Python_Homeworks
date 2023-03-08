# Задаем длину списка наполненного рандомными числами от 1 до 100.
# Вводим искомое число X. Программа должна вывести в консоль сколько раз
# встречается в заданном списке искомое число X, которое мы вводим с клавиатуры,
# либо выводим на экран, максимально близкое ему по значению

import random

length = int(input("Enter list size "))
newList = [random.randint(1, 100) for _ in range(length)]
print(newList)
num = int(input("Enter number to check "))

if newList.count(num) > 0:
    print(f"{newList.count(num)} match(es)")
else:
    numR = numL = num
    flag = True
    while (flag):
        numR += 1
        numL -= 1
        if numR in newList:
            print(f"No matches! Nearest number: {numR}")
            flag = False
        if numL in newList:
            print(f"No matches! Nearest number: {numL}")
            flag = False
