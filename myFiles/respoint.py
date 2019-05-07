# Created by Fedyuk Yuliya
# areasPoint
# 28.10.2018


def checkInputData():
    inData = input()
    try:
        data = float(inData)
    except ValueError:
        print("Недопустимый ввод. " + "'" + inData +
              "'" + " не является действительным числом.")
        exit(0)
    return data


def isPointInArea(firstArg, secondArg):
    return (-2 * firstArg + secondArg - 2 < 0 and 2*firstArg + 2*secondArg < 0 and (firstArg + 1)**2 + (secondArg - 1)**2 - 4 >= 0) or \
           (-2*firstArg + secondArg - 2 >= 0 and 2*firstArg + 2*secondArg >= 0 and (firstArg + 1)**2 + (secondArg - 1)**2 - 4 <= 0)


print("Введите значение x: ")
oneV = checkInputData()
print("Введите значение y: ")
twoV = checkInputData()
print("Точка принадлежит квадрату: ", (isPointInArea(oneV, twoV)))
