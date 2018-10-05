# Created by Samohin Artem
# Date 2018-09-10
# Task Description: http://www.hostedredmine.com/issues/775372

# проверка входных данных
def checkInput():
    a = input()
    for i in range(0, len(a)):
        if len(a.split(" ")) != 2:
            print("Ошибка! Строка должна состоять из двух слов!")
            exit(0)
    return a


s = checkInput()
print(s[s.find(" ")+ 1:len(s)] + " " + s[0:s.find(" ")])