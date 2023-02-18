# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками (то есть разломить 
# шоколадку на два прямоугольника).

print("Enter cholcolate size")
chocoLen = int(input("Length: "))
chocoWid = int(input("Width: "))
chocoSquares = int(input("Enter number of squares to cut: "))

if chocoSquares >= chocoLen * chocoWid:
    print("Error!")
elif chocoSquares % chocoLen == 0 or chocoSquares % chocoWid == 0:
    print("Yes")
else:
    print("No")