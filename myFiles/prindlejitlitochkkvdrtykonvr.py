# Created by Olesya Bandurina
# Date 30.09.2018
# Task Description: Принадлежит ли точка квадрату

def IsPointInSquare(xValue, yValue):
    return abs(xValue) <= 1 and abs(yValue) <= 1


aValue = float(input("Введите х:"))
bValue = float(input("Введте у:"))

if IsPointInSquare(aValue, bValue):
    print("YES")
else:
    print("NO")
