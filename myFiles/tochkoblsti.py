#Исхаков Дамир
#Принадлежит ли точка области?
#01.10.2018
def isPointInArea(x, y):
    FirstLine = y < ((2 * x) + 2)
    SecondLine = y < -x
    Circle = ((x + 1)*(x + 1) + (y - 1)*(y - 1)) <= 4
    return (FirstLine and SecondLine and not Circle)\
           or (not FirstLine and not SecondLine and Circle)

x = float(input("Введите \"x\" значение = "))
y = float(input("Введите \"y\" значение = "))

if isPointInArea(x, y):
    print("YES")
else:
    print("NO")
