xStart = int(input("Введите строку начального положения шашки: "))
yStart = int(input("Введите столбец начального положения шашки: "))
xEnd = int(input("Введите строку конечного положения шашки: "))
yEnd = int(input("Введите столбец конечного положения шашки: "))


def search(x, y):
    if x <= 8:
        if (x == xEnd) and (y == yEnd):
            print("YES")
            exit(0)
        x += 1
        if y == 8:
            r = search(x, y - 1)
        else:
            if y == 1:
                r = search(x, y + 1)
            else:
                r = search(x, y + 1)
                r = search(x, y - 1)


search(xStart, yStart)
print("NO")