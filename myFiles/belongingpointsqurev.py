# Created by Samohin Artem
# Date 2018-10-23
# Task Description: http://www.hostedredmine.com/issues/775958


def checkInput():
    inData = input()
    try:
        data = float(inData)
    except ValueError:
        print("Неверный ввод! Координата должна быть действительным числом!")
        exit(0)
    return data


def isPointInSquare(firstNum, secondNum):
    return abs(firstNum) + abs(secondNum) <= 1


X = checkInput()
Y = checkInput()

if isPointInSquare(X, Y):
    print("Точка принадлежит квадрату")
else:
    print("Точка не принадлежит квадрату")
