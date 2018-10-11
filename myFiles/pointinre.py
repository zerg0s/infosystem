# Автор: Ира Данилова
# Задача: Принадлежит ли точка области

def isPointInArea(x, y):
    lower1stLine = y < -x
    lower2stLine = y < ((2 * x) + 2)
    inCircle = ((x + 1)**2 + (y - 1)**2) <= 4
    return (lower1stLine and lower2stLine and inCircle)\
           or (not lower1stLine and not lower2stLine and inCircle)

x = float(input())
y = float(input())

if isPointInArea(x, y):
    print("YES")
else:
    print("NO")
