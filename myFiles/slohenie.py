#Исхаков Дамир
#Сложение без сложения
#27.09.2018
def inSum(x, y):
    if y != 0:
        return inSum(x + 1, y - 1)
    else:
        return x

x = int(input("Введите \"x\" значение = "))
y = int(input("Введите \"y\" значение = "))

if x < 0 or y < 0:
    print("Неккоректный ввод значения!")
else:
    print("x + y =", inSum(x, y))
