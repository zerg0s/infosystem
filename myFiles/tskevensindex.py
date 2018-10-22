# Created by Mikhail Fadeev
# Task Description: Четные индексы

def printEvensElement(listNumber):
    elementIndex = 0
    listNumberLen = len(listNumber)
    while elementIndex < listNumberLen:
        print(listNumber[elementIndex], end=" ")
        elementIndex += 2

values = input("Enter numbers through space = ")
numbers = []
for number in values.split():
    numbers.append(int(number))

printEvensElement(numbers)
