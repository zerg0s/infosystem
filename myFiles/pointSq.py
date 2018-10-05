# Ильдар Галиуллин.
# Принадлежит ли точка квадрату.
# 26.09.2018.


def isPointInSquare(x, y):
    return abs(x) + abs(y) <= 1


x1 = float(input("Введите х: "))
y1 = float(input("Введите у: "))
belong = isPointInSquare(x1, y1)
if belong:
    print("YES")
else:
    print("NO")
