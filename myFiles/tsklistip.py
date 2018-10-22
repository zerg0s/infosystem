# Created by Mikhail Fadeev
# Task Description: "Сжатие" списка

def zipListNumber(uzList):
    zipPos = 0
    elPos = 0
    while elPos < len(uzList):
        if uzList[elPos] != 0:
            uzList[zipPos], uzList[elPos] = uzList[elPos], uzList[zipPos]
            zipPos += 1
        elPos += 1

values = input("Enter numbers through space = ")
numbers = []
for number in values.split():
    numbers.append(int(number))

zipListNumber(numbers)
for number in numbers:
    print(number, end=" ")
