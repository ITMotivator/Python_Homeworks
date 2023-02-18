# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа 
# сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, 
# чем Петя и Сережа вместе?

# x (Петя) + y (Сережа) + z (Катя) = S;
# z = 2(x + y); x = y; S = 3x + 3y = 6x;
totalPaperCranes = int(input('Enter total cranes made '))
boysCranes = totalPaperCranes // 6
kateCranes = 2 * 2 * boysCranes
print(f"Kate made {kateCranes} cranes\n" +
      f"Pete made {boysCranes} cranes\n" +
      f"Serg made {boysCranes} cranes")
if totalPaperCranes % 6 > 0:
    print('One of the chidren lies!')