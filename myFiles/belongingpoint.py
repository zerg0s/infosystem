# Created by Samohin Artem
# Date 2018-09-28
# Task Description: http://www.hostedredmine.com/issues/775937

# checkInput() - функция для проверки входных данных


def checkInput():
    inData = input()
    try:
        data = float(inData)
    except ValueError:
        print("Неверный ввод! Координата должна быть действительным числом!")
        exit(0)
    return data

X = checkInput()
Y = checkInput()

if (-2*X + Y - 2 < 0 and 2*X + 2*Y < 0 and (X + 1)**2 + (Y - 1)**2 - 4 >= 0) or \
   (-2*X + Y - 2 >= 0 and 2*X + 2*Y >= 0 and (X + 1)**2 + (Y - 1)**2 - 4 <= 0):
    print("YES")
else:
    print("NO")
