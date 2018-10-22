# Created by Fedyuk Yuliya
# squaresPoint
# 18.10.2018


def checkInputData():
    inData = input()
    try:
        data = float(inData)
    except ValueError:
        print("Недопустимый ввод. " + "'" + inData +
              "'" + " не является действительным числом.")
        exit(0)
    return data


def isPointInSquare(firstNum, secondNum):
    return abs(firstNum) + abs(secondNum) <= 1


print("Введите значение x: ")
firstNum = checkInputData()
print("Введите значение y: ")
secondNum = checkInputData()
print("Точка принадлежит квадрату: ", (isPointInSquare(firstNum, secondNum)))
