# Created by Samohin Artem
# Date 2018-10-01
# Task Description: http://www.hostedredmine.com/issues/775350

# проверка входных данных


def checkInput():
    inData = input()
    count = 0
    for index in range(0, len(inData)):
        if inData[index] == 'h':
            count += 1
    if count == 2:
        print("Строка не требует изменений, так как содержит два символа 'h'")
        exit(0)
    if count < 3:
        print("Ошибка!Недостаточное количество вхождений символа 'h' в строку")
        exit(0)
    return inData


s = checkInput()
b = ""
for i in range(0, len(s)):
    if s[i] == 'h' and s.find("h") != i and s.rfind("h") != i:
        b = b + "H"
    else:
        b = b + s[i]
print(b)
