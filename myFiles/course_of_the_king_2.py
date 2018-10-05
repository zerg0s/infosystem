#Created by Grebneva Kseniya
#course_of_the_king
#14.09.2018

while True:
    
    print('Введите номер столбца и номер строки для первой клетки: ')
    
    A1 = int(input('Введите число от 1 до 8: '))
    A2 = int(input('Введите число от 1 до 8: '))
    
    print('Введите номер столбца и номер строки для второй клетки: ')
    
    B1 = int(input('Введите число от 1 до 8: '))
    B2 = int(input('Введите число от 1 до 8: '))
    
    if(A1 < 1 or A1 > 8 or A2 < 1 or A2 > 8 or B1 < 1 or B1 > 8 or B2 < 1 or B2 > 8):
        print('Числа должны быть больше 1 и меньше 8.')
    elif(A1 == B1 and A2 == B2):
        print('Вы ввели номер столбца и строки одной и той же клетки')
    elif((A1-B1) == 1 or (A1-B1) == -1 and (A2-B2) == 1 or (A2-B2) == -1):
        print('YES')
        break
    else:
        print('NO')
        break
