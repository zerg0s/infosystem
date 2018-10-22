# Created by Fedyuk Yuliya
# areasPoint
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


def isPointInArea(x, y):
    return (-2 * x + y - 2 < 0 and 2*x + 2*y < 0 and (x + 1)**2 + (y - 1)**2 - 4 >= 0) or \
           (-2*x + y - 2 >= 0 and 2*x + 2*y >= 0 and (x + 1)**2 + (y - 1)**2 - 4 <= 0)


print("Введите значение x: ")
x = checkInputData()
print("Введите значение y: ")
y = checkInputData()
print("Точка принадлежит квадрату: ", (isPointInArea(x, y)))
