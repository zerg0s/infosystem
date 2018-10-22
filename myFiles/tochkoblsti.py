#Исхаков Дамир
#Принадлежит ли точка области?
#01.10.2018
def isPointInArea(x_1, y_1):
    firstline = y_1 < ((2 * x_1) + 2)
    secondline = y_1 < -x_1
    circle = ((x_1 + 1)*(x_1 + 1) + (y_1 - 1)*(y_1 - 1)) <= 4
    return (firstline and secondline and not circle)\
           or (not firstline and not secondline and circle)

x_1 = float(input("Введите \"x_1\" значение = "))
y_1 = float(input("Введите \"y_1\" значение = "))

if isPointInArea(x_1, y_1):
    print("YES")
else:
    print("NO")
