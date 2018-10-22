# Мария Евсеева
# Количество совпадающих пар

def countEquPair(srcList):
    counter = 0
    i = 0
    while i < len(srcList):
        j = i + 1
        while j < len(srcList):
            if srcList[i] == srcList[j]:
                counter = counter + 1
            j = j + 1
        i = i + 1

    return counter

values = input("Введите числа через пробел: ")
numbers = []
for number in values.split():
    numbers.append(int(number))

print(countEquPair(numbers))
