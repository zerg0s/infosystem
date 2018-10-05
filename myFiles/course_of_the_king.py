#Created by Grebneva Kseniya
#course_of_the_king
#14.09.2018

while True:
    print('Введите номер столбца и номер строки для первой клетки: ')
    a1 = int(input('Введите число от 1 до 8: '))
    a2 = int(input('Введите число от 1 до 8: '))
    print('Введите номер столбца и номер строки для второй клетки: ')
    b1 = int(input('Введите число от 1 до 8: '))
    b2 = int(input('Введите число от 1 до 8: '))
    if(a1<1 or a1>8 or a2<1 or a2>8 or b1<1 or b1>8 or b2<1 or b2>8):
        print('Числа должны быть больше 1 и меньше 8.')
    elif(a1==b1 and a2==b2):
        print('Вы ввели номер столбца и строки одной и той же клетки')
    elif((a1-b1)==1 or (a1-b1)==-1 and (a2-b2)==1 or (a2-b2)==-1):
        print('YES')
        break
    else:
        print('NO')
        break
