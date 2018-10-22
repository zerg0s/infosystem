#Исхаков Дамир
#Принадлежит ли точка квадрату
#26.09.2018
def PointInSquare(x, y):
    return abs(x) <= 1 and abs(y) <= 1
x = float(input())
y = float(input())
if PointInSquare:
    print('NO')
else:
    print('YES')
PointInSquare(x,y)

