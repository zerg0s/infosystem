# Created by Samohin Artem
# Date 2018-09-27
# Task Description: http://www.hostedredmine.com/issues/775874

# Функция checkInput() служит для проверки входных данных


def checkInput():
    in_data = input()
    if in_data.lstrip("-").isdigit():
        data = int(in_data)
        return data
    else:
        print("Недопустимый ввод! " + "'" + in_data +
              "'" + " не является целым числом!")
        return exit(0)


# Функция sum(a, b) служит для суммирования чисел а и b


def sum(a, b):
    if int(b) != 0:
        b -= 1
        a += 1
        return sum(a, b)

    return a


print("Введите a: ")
A = checkInput()
print("Введите b: ")
B = checkInput()
print(sum(A, B))
