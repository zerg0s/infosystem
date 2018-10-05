# Created by Mikhail Fadeev
# Task Description: Принадлежит ли точка области?

def isPointInArea(x, y):
    isLowerFirstLine = y < ((2 * x) + 2)
    isLowerSecondLine = y < -x
    isInCircle = ((x + 1)*(x + 1) + (y - 1)*(y - 1)) <= 4
    return (isLowerFirstLine and isLowerSecondLine and not isInCircle)\
           or (not isLowerFirstLine and not isLowerSecondLine and isInCircle)

x = float(input("Enter \"x\" value = "))
y = float(input("Enter \"y\" value = "))

if isPointInArea(x, y):
    print("YES")
else:
    print("NO")
