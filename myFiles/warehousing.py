#Created by Olesya Bandurina
#Date 09.09.2018
#Task Description: Определите максимальное количество ноутбуков, которое может быть размещено на складе

a = int (input("Введите длину склада:"))
b = int (input("Введите ширину склада:"))
c = int (input('Введите высоту склада:'))
x = int (input("Введите длину коробки с ноутбуком:"))
y = int (input("Введите ширину коробки с ноутбуком:"))
z = int (input("Введите высоту коробки с ноутбуком:"))

n1: int = (a // x) * (b // y) * (c // z)
n2: int = (a // x) * (b // z) * (c // y)
n3: int = (a // y) * (b // a) * (c // z)
n4: int = (a // y) * (b // z) * (c // x)
n5: int = (a // z) * (b // a) * (c // y)
n6: int = (a // z) * (b // y) * (c // x)

if a >= x and b >= y and c >= z:
    if n1 > n2 and n1 > n3 and n1 > n4 and n1 > n5 and n1 > n6:
        print(n1)
    elif n2 > n3 and n2 > n4 and n2 > n5 and n2 > n6:
        print(n2)
    elif n3 > n4 and n3 > n5 and n3 > n6:
        print(n3)
    elif n4 > n5 and n4 > n6:
        print(n4)
    elif n5 > n6:
        print(n5)
    else:
        print(n6)
else:
    print(0)
