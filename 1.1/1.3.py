# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и 
# получали билет с номером. Счастливым билетом называют такой билет с шестизначным 
# номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с 
# номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, 
# которая проверяет счастливость билета.

ticketNum = int(input('Enter ticket number '))
numEnd = ticketNum % 1000
numStart = ticketNum // 1000

ones = numEnd % 10
tens = (numEnd // 10) % 10
hundreds = numEnd // 100
sumEnd = ones + tens + hundreds
ones = numStart % 10
tens = (numStart // 10) % 10
hundreds = numStart // 100
sumStart = ones + tens + hundreds

if sumEnd == sumStart:
    print("Happy ticket")
else:
    print("Not happy ticket")