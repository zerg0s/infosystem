#Created by Petr Gusev
#Chekkers
#11.09.2018

print("Введите координаты, на которых находится шашка\n")

horChecker = int(input("Введите горизонтальную координату:"))
verChecker = int(input("Введите вертикальную координату:"))

if ((horChecker + verChecker) % 2) == 1:
    print("Шашка не может стоять в данной клетке.")
    exit(1)

print("Введите конечные координаты")
horNew = int(input("Введите горизонтальную координату:"))
verNew = int(input("Введите вертикальную координату:"))

if horChecker == horNew and verChecker == verNew:
    print("Шашка остается на своем месте")
    exit()

if (horNew + verNew) >= (horChecker + verChecker) and (horNew + verNew) % 2 == 0 and verNew > verChecker:
    print("YES")
else:
    print("NO")
	