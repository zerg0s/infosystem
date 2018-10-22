# Ильдар Галиуллин.
# Принадлежит ли точка области.
# 26.09.2018.

import math


def isPointInArea(x, y):
    return (y >= -x and
            y >= 2*x + 2 and
            (y <= math.sqrt(4 - (x + 1) ** 2) + 1 and
             y >= -math.sqrt(4 - (x + 1) ** 2) + 1)) \
            or (y <= -x and
                y <= 2*x + 2 and
                y <= - math.sqrt(4 - (x + 1) ** 2) + 1)


x1 = float(input("Введите х: "))
y1 = float(input("Введите у: "))
belong = isPointInArea(x1, y1)
if belong:
    print("YES")
else:
    print("NO")
