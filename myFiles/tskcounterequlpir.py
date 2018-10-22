# Created by Mikhail Fadeev
# Task Description: Количество совпадающих пар

def getNumberEqualPair(listNumber):
    numberPair = 0
    elementIndex = 0
    while elementIndex < len(listNumber):
        extendIndex = elementIndex + 1
        while extendIndex < len(listNumber):
            if listNumber[elementIndex] == listNumber[extendIndex]:
                numberPair += 1
            extendIndex += 1
        elementIndex += 1
    return numberPair

values = input("Enter numbers through space = ")
numbers = []
for number in values.split():
    numbers.append(int(number))

result = getNumberEqualPair(numbers)
print(result)
