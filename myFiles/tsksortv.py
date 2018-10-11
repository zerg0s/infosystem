# Created by Samohin Artem
# Date 2018-10-10
# Task Description: http://www.hostedredmine.com/issues/777995


# Функция checkInput() служит для ввода и проверки входных данных

def checkInput():
    inData = input()
    parseData = list()
    seqList = inData.split(" ")
    for index in range(0, len(seqList)):
        try:
            parseData.append(int(seqList[index]))
        except ValueError:
            print("Ошибка! Последовательность содержит не только целые числа")
            exit(0)
    return parseData


myList = checkInput()
myList.sort(key=lambda valEnd: valEnd == 0)
print(' '.join(str(e) for e in myList))
