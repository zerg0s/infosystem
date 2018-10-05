# Created by Fedyuk Yuliya
# Сheckers
# 19.09.2018

firstV = int(input("Введите номер вертикали для первой шашки от 1 до 8: "))
firstH = int(input("Введите номер горизонтали для первой шашки от 1 до 8: "))
secondV = int(input("Введите номер вертикали для второй шашки от 1до 8: "))
secondH = int(input("Введите номер горизонтали для второй шашки от 1 до 8: "))

if (firstH < secondH and
    (secondH - firstH >= abs(secondV - firstV)) and
    ((firstV % 2 == secondV  % 2 and (secondH - firstH) % 2 == 0) or
    (firstV % 2 != secondV  % 2 and (secondH - firstH) % 2 != 0))
): 
    print("YES")
else:
    print("NO")
	
