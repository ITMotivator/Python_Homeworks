# Требуется вывести все целые степени двойки (т.е. числа вида 2k),
# не превосходящие числа N.

num = int(input("Enter any number "))
k = 0
while 2 ** k <= num:
    print(2 ** k, end=' ')
    k += 1
