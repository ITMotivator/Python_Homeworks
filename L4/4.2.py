# В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, 
# причем кусты высажены только по окружности. Таким образом, у каждого куста есть 
# ровно два соседних. Всего на грядке растет N кустов. Эти кусты обладают разной 
# урожайностью, поэтому ко времени сбора на них выросло различное число ягод – 
# на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, 
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать 
# за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

import random

bashesQnt = int(input("Enter quantity of bashes "))
berries = [random.randint(50, 100) for _ in range(bashesQnt)]
print(berries)
max = 0
for i in range(bashesQnt):
    j = 0 if i + 1 == bashesQnt else i + 1
    sumof3 = berries[i] + berries[j] + berries[i-1]
    if sumof3 > max:
        max = sumof3
        maxInd = i
print(max, maxInd)        
