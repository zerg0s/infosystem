# Created by Samohin Artem
# Date 2018-10-22
# Task Description: http://www.hostedredmine.com/issues/779610


# Функция checkInput() служит для ввода и проверки входных данных

def checkInput():
    inData = input()
    parseData = list()
    seqList = inData.split(" ")
    for index in range(0, len(seqList)):
        try:
            parseData.append(float(seqList[index]))
        except ValueError:
            print("Ошибка! Последовательность содержит не только числа")
            exit(0)
    return parseData


myList = checkInput()
maxValue = myList[0]
maxIndex = 0
for i in range(1, len(myList)):
    if maxValue <= myList[i]:
        maxValue = myList[i]
        maxIndex = i

print(str(maxValue) + " " + str(maxIndex))
