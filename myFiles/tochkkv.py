# Created  by Maltsev Alexey
# 9.10.18
# Принадлежит ли точка квадрату?

def isPointInSquare(x, y):
    return abs(x) + abs(y) <= 1
x = float(input("Enter the coordinate x: "))
y = float(input("Enter the coordinate y: "))
if (isPointInSquare(x, y)):
    print("YES")
else:
    print("NO")
