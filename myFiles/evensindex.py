# Мария Евсеева
# Четные индексы

def printEvensIndex(srcList):
    i = 0
    while i < len(srcList):
        print(srcList[i], end=" ")
        i = i + 2

values = input("Введите числа через пробел: ")
numbers = []
for number in values.split():
    numbers.append(int(number))

printEvensIndex(numbers)
