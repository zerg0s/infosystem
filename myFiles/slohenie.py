#Исхаков Дамир
#Сложение без сложения
#27.09.2018
def inSum(xone, yone):
    if yone != 0:
        return inSum(xone + 1, yone - 1)
    else:
        return xone

xone = int(input("Введите \"xone\" значение = "))
yone = int(input("Введите \"yone\" значение = "))

if xone < 0 or yone < 0:
    print("Неккоректный ввод значения!")
else:
    print("xone + yone =", inSum(xone, yone))
