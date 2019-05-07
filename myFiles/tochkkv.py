# Created  by Maltsev Alexey
# 9.10.18
# Принадлежит ли точка квадрату?

theXcoordinate = float(input("Введите x: "))
theYcoordinate = float(input("Введите y: "))
def isPointInSquare(theXcoordinate, theYcoordinate):
    return abs(theXcoordinate) + abs(theYcoordinate) <= 1
if (isPointInSquare(theXcoordinate, theYcoordinate)):
    print("YES")
else:
    print("NO")
