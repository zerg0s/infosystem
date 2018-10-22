# Мария Евсеева
# "Сжатие" списка

def zipList(unzipList):
    lastPos = 0
    curPos = 0
    while curPos < len(unzipList):
        if unzipList[curPos] != 0:
            unzipList[lastPos], unzipList[curPos] =\
                                                 unzipList[curPos],\
                                                 unzipList[lastPos]
            lastPos = lastPos + 1
        curPos = curPos + 1

values = input("Введите числа через пробел: ")
numbers = []
for number in values.split():
    numbers.append(int(number))

zipList(numbers)
for number in numbers:
    print(number, end=" ")
