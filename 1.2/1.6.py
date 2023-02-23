# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных
# числа i и j (i,j≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

sum = int(input("Enter sum of numbers "))
product = int(input("Enter product of numbers "))
flag = True
x = 0
y = 0
for i in range(2, 1000):
    for j in range(2, 1000):
        if i + j == sum and i * j == product:
            flag = False
            x = i
            y = j
            break
        else:
            j += 1
    if flag == False:
        break
    else:
        i += 1
print(f"x = {x}, y = {y}")

