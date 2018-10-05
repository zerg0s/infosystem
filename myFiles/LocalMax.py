# Мария Евсеева
# Наименьшее расстояние между локальными максимумами

valueList = []
print("Введите числа (0 для завершения)")
while True:
    value = int(input())
    if value == 0:
        break
    valueList.append(value)

if len(valueList) < 3:
    print(0)
    exit()

currentMaxPos = 0
prevMaxPos = 0
minRange = 0

i = 1
while i < (len(valueList) - 1):
    if valueList[i - 1] < valueList[i] and valueList[i] > valueList[i + 1]:
        prevMaxPos = currentMaxPos
        currentMaxPos = i
        if currentMaxPos != 0 and prevMaxPos != 0:
            if minRange == 0:
                minRange = currentMaxPos - prevMaxPos
            elif minRange > currentMaxPos - prevMaxPos:
                minRange = currentMaxPos - prevMaxPos
    i = i + 1

print(minRange)
