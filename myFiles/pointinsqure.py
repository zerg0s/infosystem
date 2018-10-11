# Автор: Ира Данилова
# Задача: Принадлежит ли точка квадрату

def isPointInSquare(x, y):
    in1stPlane = (y <= (-x + 1)) and (y >= (-x - 1))
    in2stPlane = (y <= (x + 1)) and (y >= (x - 1))
    return in1stPlane and in2stPlane

x = float(input())
y = float(input())

if isPointInSquare(x, y):
    print("YES")
else:
    print("NO")
