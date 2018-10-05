# Created by Mikhail Fadeev
# Task Description: Найти второй максимум

values = []
isNullNotEntered = True
while isNullNotEntered:
    inputValue = input()
    if inputValue.lstrip("-").isdigit():
        value = int(inputValue)
        if value == 0:
            isNullNotEntered = False
        else:
            values.append(value)
    else:
        print("Invalid input value!")
        exit()

firstMax = 0
secondMax = 0
if len(values) >= 2:
    firstMax = values[0]
    secondMax = values[1]
    if firstMax < secondMax:
        firstMax, secondMax = secondMax, firstMax

    i = 2
    while i < len(values):
        if values[i] > firstMax:
            secondMax = firstMax
            firstMax = values[i]
        elif values[i] > secondMax:
            secondMax = values[i]
        i = i + 1

print(secondMax)
