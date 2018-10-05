# Created by Samohin Artem
# Date 2018-09-19
# Task Description: http://www.hostedredmine.com/issues/773476

"""
Функция check_input()
Выполняет проверку входных данных
"""


def check_input():
    in_data = input()
    if in_data.isdigit():
        data = int(in_data)
        return data
    print("Недопустимый ввод! " + "'" + in_data +
          "'" + " не является натуральным числом!")
    return exit(0)

first_value = check_input()
second_value = check_input()

if first_value <= second_value:
    print("Первое число должно быть больше второго!")
    exit(0)

while first_value != second_value:
    if(first_value % 2 == 0) and (first_value/2 - second_value > 0):
        first_value = first_value/2
        print(":2")
    if (first_value/2 - second_value < 0) or (first_value % 2 != 0) or \
       (first_value - second_value == 1):
        first_value = first_value - 1
        print("-1")
