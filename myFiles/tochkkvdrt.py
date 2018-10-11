#Исхаков Дамир
#Принадлежит ли точка квадрату?
#02.10.2018
def isPointInSquare(x, y):
    First = (y <= (x + 1)) and (y >= (x - 1))
    Second = (y <= (-x + 1)) and (y >= (-x - 1))
    return First and Second

x = float(input("Введите \"x\" значение = "))
y = float(input("Введите \"y\" значение = "))

if isPointInSquare(x, y):
    print("YES")
else:
    print("NO")
