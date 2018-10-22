# Created by Mikhail Fadeev
# Task Description: Больше соседей

def getNeighborsCount(listNumber):
    neighborsNumber = 0
    for elIndex in range(1, (len(listNumber) - 1)):
        if listNumber[elIndex] > listNumber[elIndex - 1]\
           and listNumber[elIndex] > listNumber[elIndex + 1]:
            neighborsNumber += 1
    return neighborsNumber

values = input("Enter numbers through space = ")
numbers = []
for number in values.split():
    numbers.append(int(number))

print(getNeighborsCount(numbers))
