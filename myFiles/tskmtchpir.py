# Created by Samohin Artem
# Date 2018-10-08
# Task Description: http://www.hostedredmine.com/issues/777932

# Input data and check data


def initArray():
    inData = input()
    myList = inData.split(" ")
    for index in range(0, len(myList)):
        try:
            parseData = float(myList[index])
        except ValueError:
            print("Неверный ввод! Последовательность содержит не только числа")
            exit(0)
    return myList


seqNum = initArray()
countPair = 0
for i in range(0, len(seqNum) - 1):
    for j in range(i + 1, len(seqNum)):
        if seqNum[i] == seqNum[j]:
            countPair += 1
print(countPair)
