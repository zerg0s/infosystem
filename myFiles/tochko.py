# Created  by Maltsev Alexey
# 11.10.18
# Принадлежит ли точка области?

x = float(input("Введите x: "))
y = float(input("Введите y: "))
def isPointInArea(x, y):
    return((y >= -x and y >= 2*x+2 and (x+1)**2+(y-1)**2 <= 4) or
           (y <= -x and y <= 2*x+2 and (x+1)**2+(y-1)**2 >= 4))
if(isPointInArea(x, y)):
    print("YES")
else:
    print("NO")
