#Мария Евсеева
#Принадлежит ли точка области?

def isPointInArea(x, y):
    pointIsLowerFirstLine = y < ((2 * x) + 2)
    pointIsLowerSecondLine = y < -x
    pointIsOutCircle = ((x + 1)**2 + (y - 1)**2) >= 4
    pointIsInCircle = ((x + 1)**2 + (y - 1)**2) <= 4
    return (pointIsLowerFirstLine and pointIsLowerSecondLine\
            and pointIsOutCircle) or ((not pointIsLowerFirstLine)\
            and (not pointIsLowerSecondLine) and pointIsInCircle)

x = float(input("Введите x: "))
y = float(input("Введите y: "))

if isPointInArea(x, y) == True:
    print("YES")
else:
    print("NO")
