# Created by Olesya Bandurina
# Date 30.09.2018
# Task Description: Принадлежит ли точка квадрату


def IsPointInSquare(x, y):
    return abs(x) <= 1 and abs(y) <= 1


a = float(input("Введите х:"))
b = float(input("Введте у:"))

if IsPointInSquare(a, b):
    print("YES")
else:
    print("NO")
