#Мария Евсеева
#Принадлежит ли точка квадрату?

def isPointInSquare(x, y):
    pointInFirstPlane = (y <= (x + 1)) and (y >= (x - 1))
    pointInSecondPlane = (y <= (-x + 1)) and (y >= (-x - 1))
    return pointInFirstPlane and pointInSecondPlane

x = float(input("Введите x: "))
y = float(input("Введите y: "))

if isPointInSquare(x, y) == True:
    print("YES")
else:
    print("NO")
