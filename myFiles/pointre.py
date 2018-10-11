def PointArea(x, y):
    FirstLine = y < ((2 * x) + 2)
    SecondLine = y < -x
    Circle = ((x + 1)*(x + 1) + (y - 1)*(y - 1)) <= 4
    return (FirstLine and SecondLine and not Circle)\
        or (not FirstLine and not SecondLine and Circle)

x = float(input("Введите \"x\" = "))
y = float(input("Введите \"y\" = "))

if PointArea(x, y):
    print("YES")
else:
    print("NO")
