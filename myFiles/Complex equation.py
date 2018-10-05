# Created by Fedyuk Yuliya
# Complex equation
# 13.09.2018

# Получаем значения числа
a = int(input("Введите значение числа a: "))
b = int(input("Введите значение числа b: "))
c = int(input("Введите значение числа c: "))
d = int(input("Введите значение числа d: "))

# Прописываем условия и результат
if ((d == 0) and (c == 0)):
    print("c и d не могут одновременно равняться нулю - запрет делить на ноль")
elif ((a == 0) and (b == 0)):
    print("INF")
elif (a == 0):
    print("NO")
elif (c == 0):
    print (-b/a)
elif (b/a == d/c):
    print("NO")
else:
    print(-b/a)
