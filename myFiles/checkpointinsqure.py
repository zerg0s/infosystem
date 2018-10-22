# Мария Евсеева
# Принадлежит ли точка квадрату?

def isPointInSquare(xVal, yVal):
    pointInFirstPlane = (yVal <= (xVal + 1)) and (yVal >= (xVal - 1))
    pointInSecondPlane = (yVal <= (-xVal + 1)) and (yVal >= (-xVal - 1))
    return pointInFirstPlane and pointInSecondPlane

xInputVal = float(input("Введите x: "))
yInputVal = float(input("Введите y: "))

if isPointInSquare(xInputVal, yInputVal):
    print("YES")
else:
    print("NO")
