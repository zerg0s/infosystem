# Created by Mikhail Fadeev
# Task Description: Принадлежит ли точка квадрату?

def isPointInSquare(xPoint, yPoint):
    inFirstPlane = (yPoint <= (xPoint + 1)) and (yPoint >= (xPoint - 1))
    inSecondPlane = (yPoint <= (-xPoint + 1)) and (yPoint >= (-xPoint - 1))
    return inFirstPlane and inSecondPlane

xInputPoint = float(input("Enter \"x\" value = "))
yInputPoint = float(input("Enter \"y\" value = "))

if isPointInSquare(xInputPoint, yInputPoint):
    print("YES")
else:
    print("NO")
