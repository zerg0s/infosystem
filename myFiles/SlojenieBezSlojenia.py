def summa(a, b):
    s = 0
    if a != 0:
        a -= 1
        s += 1
    if b != 0:
        b -= 1
        s += 1
    return 0 if s == 0 else s + summa(a, b)

x = int(input("Введите первое слагаемое: "))
y = int(input("Введите второе слагаемое: "))
print(summa(x, y))
