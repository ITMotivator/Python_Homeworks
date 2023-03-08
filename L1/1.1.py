# Найдите сумму цифр трехзначного числа.
number = int(input('Enter 3digit number '))
ones = number % 10
tens = (number // 10) % 10
hundreds = number // 100
sum = ones + tens + hundreds
print(f"Number digits sum = {sum}")