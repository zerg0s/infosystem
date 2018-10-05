# Created by Samohin Artem
# Date 2018-10-01
# Task Description: http://www.hostedredmine.com/issues/775874

# Функция checkInput() служит для проверки входных данных


def checkInput():
    inData = input()
    if inData.lstrip("-").isdigit():
        data = int(inData)
        return data
    print("Недопустимый ввод! " + "'" + inData +
          "'" + " не является целым числом!")
    return exit(0)


# Функция sum(a, b) служит для суммирования чисел а и b


def sumNumbers(inA, inB):
    if int(inB) != 0:
        inB -= 1
        inA += 1
        return sumNumbers(inA, inB)
    return inA


print("Введите a: ")
A = checkInput()
print("Введите b: ")
B = checkInput()
print(sumNumbers(A, B))
