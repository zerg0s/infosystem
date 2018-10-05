"""
Created by Samohin Artem
Date 2018-09-17
Task Description: http://www.hostedredmine.com/issues/773101
"""

"""
Функция check_input() служит для проверки входных данных
"""


def check_input():
    in_data = input()
    if in_data.lstrip("-").isdigit():
        data = int(in_data)
        return data
    print("Недопустимый ввод! " + "'" + in_data +
          "'" + " не является целым числом!")
    exit(0)


"""
Функция check_output() служит для проверки выходных данных
"""


def check_output(value_1, value_2):
    try:
        dif = int('%g' % (-value_2 / value_1))
    except ValueError:
        print("NO")
        exit(0)
    return dif


print("Решение уравнения: (ax+b)/(cx+d) = 0")
print("Введите коэффициент а:")
A = check_input()
print("Введите коэффициент b:")
B = check_input()
print("Введите коэффициент c:")
C = check_input()
print("Введите коэффициент d:")
D = check_input()
if (C == 0) and (D == 0):
    print("NO")
    exit(0)
elif (A == 0) and (B == 0):
    print('INF')
    exit(0)
elif A == 0:
    print('NO')
    exit(0)
elif C == 0:
    print(str(check_output(A, B)))
    exit(0)
elif B/A == D/C:
    print('NO')
    exit(0)
else:
    print(str(check_output(A, B)))
    exit(0)
