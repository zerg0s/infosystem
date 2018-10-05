# Created by Mikhail Fadeev
# Task Description: Принадлежит ли точка квадрату?

def isPointInSquare(x, y):
    inFirstPlane = (y <= (x + 1)) and (y >= (x - 1))
    inSecondPlane = (y <= (-x + 1)) and (y >= (-x - 1))
    return inFirstPlane and inSecondPlane

x = float(input("Enter \"x\" value = "))
y = float(input("Enter \"y\" value = "))

if isPointInSquare(x, y):
    print("YES")
else:
    print("NO")
