#Created by Grebneva Kseniya
#checkers
#21.09.2018

x1 = int(input("Введите вертикаль клетки, где стоит шашка: "))
x2 = int(input("Введите горизонталь клетки, где стоит шашка: "))
y1 = int(input("Введите вертикаль клетки, куда шашка должна попасть: "))
y2 = int(input("Введите горизонталь клетки, куда шашка долна попасть: "))

if(x1>0 and x1<9 and x2>0 and x2<9 and y1>0 and y1<9 and y2>0 and y2<9):
    if((x2 < y2) and (y2 - x2 >= abs(y1 - x1)) and
        ((x1 % 2 == y1 % 2 and (y2 - x2) % 2 == 0) or
        (x1 % 2 != y1 % 2 and (y2 - x2) % 2 != 0))):
        print("YES")
    elif(y1 == 8):
        print("Шашка становится дамкой.")
    else:
        print("NO")
