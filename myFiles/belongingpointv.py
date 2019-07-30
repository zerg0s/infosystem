# Created by Samohin Artem
# Date 2018-10-23
# Task Description: http://www.hostedredmine.com/issues/775937


def checkInput():
    inData = input()
    try:
        parseData = float(inData)
    except ValueError:
        print("Неверный ввод! Координата должна быть действительным числом!")
        exit(0)
    return parseData


def isPointInArea(firstNum, secondNum):
    return (-2*X + Y - 2 < 0 and 2*X + 2*Y < 0 and (X + 1)**2 + (Y - 1)**2 - 4 >= 0) or \
           (-2*X + Y - 2 >= 0 and 2*X + 2*Y >= 0 and (X + 1)**2 + (Y - 1)**2 - 4 <= 0)


X = checkInput()
Y = checkInput()

if isPointInArea(X, Y):
    print("YES")
else:
    print("NO")
