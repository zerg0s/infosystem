# Created by Mikhail Fadeev
# Task Description: Наименьшее расстояние между локальными максимумами

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

minDistance = 0
if len(values) >= 3:
    leftMaxPos = 0
    rightMaxPos = 0

    i = 1
    while i < (len(values) - 1):
        if values[i - 1] < values[i] and values[i] > values[i + 1]:
            leftMaxPos = rightMaxPos
            rightMaxPos = i
            if rightMaxPos != 0 and leftMaxPos != 0:
                currentDistance = rightMaxPos - leftMaxPos
                if minDistance == 0:
                    minDistance = currentDistance
                elif minDistance > currentDistance:
                    minDistance = currentDistance
        i = i + 1

print(minDistance)
