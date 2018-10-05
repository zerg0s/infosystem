# Created by Samohin Artem
# Date 2018-09-28
# Task Description: http://www.hostedredmine.com/issues/775958

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

if abs(X) + abs(Y) <= 1:
    print("YES")
else:
    print("NO")
