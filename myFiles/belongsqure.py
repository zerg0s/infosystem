# Аверина Мария
# Принадлежит ли точка квадрату
# 12.10.2018


def isPointInSquare(num1, num2):
    return abs(num1) + abs(num2) <= 1


a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))

if isPointInSquare(a, b):
    print("YES")
else:
    print("NO")
