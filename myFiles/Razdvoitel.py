# Created by Alexey Maltsev
# 18.09.18
# Раздвоитель

a = int(input('Введите число a :'))
b = int(input('Введите число b :'))

while a >= b + 1:
    if a % 2 == 0 and (a / b) >= 2:
        a = int(a / 2)
        print(":2")
        #print(a)
    else:
        a = int(a - 1)
        print("-1")
        #print(a)
