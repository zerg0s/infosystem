import math

count = 0
a = []
while count < 4:
    a.append(int(input("Введите номера сток и столбцов в порядке X1,Y1 и X2,Y2. После каждого числа enter: ")))
    count += 1


def near(x, y):
    if (math.fabs(x-y) == 1) or (x-y == 0):
        return 1
    else:
        return 0


def solve(x1, y1, x2, y2):
    if near(x1, x2) and near(y1, y2):
        print("YES")
    else:
        print("NO")


solve(a[0], a[1], a[2], a[3])