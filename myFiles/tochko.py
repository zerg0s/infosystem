# Created  by Maltsev Alexey
# 11.10.18
# Принадлежит ли точка области?

x = float(input("Введите x: "))
y = float(input("Введите y: "))
def isPointInArea(x, y):
    return (2 ** 2 >= (abs(x + 1) ** 2) + (abs(y - 1) ** 2)) and (y >= 2 * x + 2) and (y >= -x) or \
           ((2 ** 2 == (abs(x + 1) ** 2) + (abs(y - 1) ** 2))
            or not (2 ** 2 >= (abs(x + 1) ** 2) + (abs(y - 1) ** 2))) and \
           (y <= 2 * x + 2) and (y <= -x)
if (isPointInArea(x, y)):
    print("YES")
else:
    print("NO")
