# Created by Samohin Artem
# Date 2018-10-08
# Task Description: http://www.hostedredmine.com/issues/777974

# Ввели, проверили, отсортировали,напечатали
inData = input()
parseData = list()
myList = inData.split(" ")
for index in range(0, len(myList)):
    try:
        parseData.append(float(myList[index]))
    except ValueError:
        print("Неверный ввод! Последовательность содержит не только числа")
        exit(0)
print([parseData[i] for i in range(0, len(parseData), 2)])
