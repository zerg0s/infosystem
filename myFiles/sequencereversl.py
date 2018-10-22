# Created by Fedyuk Yuliya
# sequence reversal
# 12.10.2018


def checkInput():
    inData = input()
    if inData.lstrip("-").isdigit():
        data = int(inData)
        return data
    print("Ошибка. " + "'" + inData +
          "'" + " не является целым числом.")
    return exit(0)


def reverse():
    print("Введите целое число. Для прекращения ввода введите ноль: ")
    seq = checkInput()
    if seq != 0:
        reverse()
    print(seq)


reverse()
