# Created by Fedyuk Yuliya
# phoneNumb
# 01.11.2018


def makeNormal(strochka):
    strochka = strochka.replace('(', '').replace(')', '').replace('-', '')
    if len(strochka) == 11:
        strochka = strochka[1:]
    elif len(strochka) == 12:
        strochka = strochka[2:]
    elif len(strochka) == 7:
        strochka = '495' + strochka
    else:
        print("Неверное введен номер!!!")
        return 0
    return strochka


def equals(origNum, eqNum):
    if origNum == eqNum:
        print("YES")
    else:
        print("NO")


originalNum = makeNormal(input("Введите номера телефонов: "))
firstNum = makeNormal(input())
secondNum = makeNormal(input())
thirdNum = makeNormal(input())
equals(originalNum, firstNum)
equals(originalNum, secondNum)
equals(originalNum, thirdNum)
