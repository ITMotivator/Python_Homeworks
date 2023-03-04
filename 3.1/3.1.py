# Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.

def raiseToPower(a, b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    else:
        return raiseToPower(a, b - 1) * a


print(raiseToPower(3, 5))
