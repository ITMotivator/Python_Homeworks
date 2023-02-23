# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

import random

num = random.randint(3, 10)
print(num)
countOne = 0;
countZero = 0;
for i in range(num):
    side = random.randint(0, 1)
    if side == 0: 
        countZero += 1
    else:
        countOne += 1
    print(side, end=' ')
print (f"\n{countZero if countZero < countOne else countOne}")
