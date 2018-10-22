# Мария Евсеева
# Больше соседей

def countNeighbors(srcList):
    counter = 0
    i = 1
    while i < (len(srcList) - 1):
        if srcList[i] > srcList[i - 1] and srcList[i] > srcList[i + 1]:
            counter = counter + 1
        i = i + 1
    return counter

values = input("Введите числа через пробел: ")
numbers = []
for number in values.split():
    numbers.append(int(number))

print(countNeighbors(numbers))
