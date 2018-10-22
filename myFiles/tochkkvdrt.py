#Исхаков Дамир
#Принадлежит ли точка квадрату?
#02.10.2018
def isPointInSquare(x_1, y_1):
    first = (y_1 <= (x_1 + 1)) and (y_1 >= (x_1 - 1))
    second = (y_1 <= (-x_1 + 1)) and (y_1 >= (-x_1 - 1))
    return first and second

x_1 = float(input("Введите \"x_1\" значение = "))
y_1 = float(input("Введите \"y_1\" значение = "))

if isPointInSquare(x_1, y_1):
    print("YES")
else:
    print("NO")
