# Created by Samohin Artem
# Date 2018-10-08
# Task Description: http://www.hostedredmine.com/issues/777953

# Input data and check data


def initArray():
    inData = input()
    parseData = list()
    myList = inData.split(" ")
    if len(myList) < 3:
        print("Последовательность содержит менее 3 элементов!")
        exit(0)
    for index in range(0, len(myList)):
        try:
            parseData.append(float(myList[index]))
        except ValueError:
            print("Неверный ввод! Последовательность содержит не только числа")
            exit(0)
    return parseData


seqNum = initArray()
countPair = 0
i = 1
while i != len(seqNum)-1:
    if(seqNum[i-1] < seqNum[i]) and (seqNum[i+1] < seqNum[i]):
        countPair += 1
    i += 1
print(countPair)
