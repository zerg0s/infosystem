def PointSquare(x, y):
    FirstPlane = (y <= (x + 1)) and (y >= (x - 1))
    SecondPlane = (y <= (-x + 1)) and (y >= (-x - 1))
    return FirstPlane and SecondPlane

x = float(input("Введите \"x\" = "))
y = float(input("Введите \"y\" = "))

if PointSquare(x, y):
    print("YES")
else:
    print("NO")
