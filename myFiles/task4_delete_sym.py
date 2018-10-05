# Created by Samohin Artem
# Date 2018-09-10
# Task Description: http://www.hostedredmine.com/issues/775327

# проверка входных данных
def checkInput():
    a = input()
    for i in range(0, len(a)):
        if a[i] == "@":
            return a
    print("Ошибка! Строка не содержит ни одного символа '@'")
    exit(0)


s = checkInput()
b = ""

for i in range(0, len(s)):
    if s[i] != "@":
        b = b + s[i]
print(b)
