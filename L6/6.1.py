# Заполните массив элементами арифметической прогрессии. Её первый элемент, 
# разность и количество элементов нужно ввести с клавиатуры. Формула для получения 
# n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

firstEl = int(input("Enter progression 1st elem "))
step = int(input("Enter progression step "))
length = int(input("Enter progression length "))
progressionList = []

current = firstEl
for i in range(1, length + 1):
    current = firstEl + (i - 1) * step
    progressionList.append(current)
     
print(progressionList)