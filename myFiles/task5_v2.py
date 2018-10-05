# Created by Samohin Artem
# Date 2018-09-19
# Task Description: http://www.hostedredmine.com/issues/773474


"""
Функция check_input()
Выполняет проверку входных данных
"""


def checkInput():
    inData = input()
    try:
        data = float(inData)
    except ValueError:
        print("Недопустимый ввод! " + "'" + inData +
              "'" + " не является действительным числом!")
        exit(0)
    return data


first_run = checkInput()
second_run = checkInput()
if first_run >= second_run:
    print("Первое число должно быть меньше второго!")
    exit(0)
day = 1  # так как в первый день он пробежал х км
while first_run < second_run:
    first_run = first_run + first_run*0.1
    day = day + 1
print(day)
