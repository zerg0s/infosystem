#Powered by Maltsev Alexey
#09.09.18
#Ход шашки

aV = int(input('Введите значение по вертикали от 1 до 8 для первой точки: '))
aH = int(input('Введите значение по горизонтали от 1 до 8 для первой точки: '))
bV = int(input('Введите значение по вертикали от 1 до 8 для второй точки: '))
bH = int(input('Введите значение по горизонтали от 1 до 8 для второй точки: '))

dA = aV + aH
dB = bV + bH
if dA > dB:
    print("NO")
else:
    c = dA % 2
    d = dB % 2
    if c == d:
        print('YES')
    else:
        print('NO')
        