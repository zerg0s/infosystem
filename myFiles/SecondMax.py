# Мария Евсеева
# Второй максимум

valueList = []
print("Введите числа (0 для завершения)")
while True:
    value = int(input())
    if value == 0:
        break;
    valueList.append(value)

if len(valueList) < 2:
    print(0)
    exit()

firstMax = valueList[0]
secondMax = valueList[1]
if firstMax < secondMax:
    firstMax, secondMax = secondMax, firstMax

i = 2
while i < len(valueList):
    if valueList[i] > firstMax:
        secondMax, firstMax = firstMax, valueList[i]
    elif valueList[i] > secondMax:
        secondMax = valueList[i]
    i = i + 1

print(secondMax)
