# Created by Mikhail Fadeev
# Task Description: Принадлежит ли точка области?

def isPointInArea(xPoint, yPoint):
    isLowerFirstLine = yPoint <= ((2 * xPoint) + 2)
    isUpperFirstLine = yPoint >= ((2 * xPoint) + 2)
    isLowerSecondLine = yPoint <= -xPoint
    isUpperSecondLine = yPoint >= -xPoint
    isInCircle = ((xPoint + 1)*(xPoint + 1) + (yPoint - 1)*(yPoint - 1)) <= 4
    return (isLowerFirstLine and isLowerSecondLine and not isInCircle)\
           or (isUpperFirstLine and isUpperSecondLine and isInCircle)

xInputPoint = float(input("Enter \"x\" value = "))
yInputPoint = float(input("Enter \"y\" value = "))

if isPointInArea(xInputPoint, yInputPoint):
    print("YES")
else:
    print("NO")
