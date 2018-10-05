# Created by Samohin Artem
# Date 2018-10-03
# Task Description: http://www.hostedredmine.com/issues/775895

offset = 0

# Функция checkInput() служит для проверки входных данных


def checkInput():
    inData = input()
    if inData.lstrip("-").isdigit():
        data = int(inData)
        return data

    print("Недопустимый ввод! " + "'" + inData +
          "'" + " не является целым числом!")
    return exit(0)


# Функция swapList() - для записи последовательности в противоположном порядке


def swapList(prelast):
    global offset
    try:
        swapList.counter += 1
    except AttributeError:
        swapList.counter = 0
    newData = checkInput()
    if newData != 0 and prelast != 0:
        if newData < prelast:
            offset = 1
        else:
            offset = -1
    if newData != 0:
        swapList(newData)
    if newData == 0:
        i = 0
        print("0")
        while i != swapList.counter + 1:
            print(str(prelast + offset*i))
            i += 1
        return


print("Введите последовательность целых чисел (0-окончание ввода):")
a = checkInput()
if a != 0:
    swapList(a)
else:
    print("Последовательность состоит из одного числа - 0!")
    exit(0)
