# Created by Fedyuk Yuliya
# SecondMaximum
# 24.09.2018
# Получаем значения последовательности

def checkInputData():
    in_data = input()
    if in_data.isdigit():
        data = int(in_data)
        return data
    print("Недопустимый ввод! " + "'" + in_data +
          "'" + " не является целым неотрицательным числом!")
    return exit(0)


# Получаем значения последовательности
print("Введите последовательность чисел, для окончания ввода введите ноль: ")
i = 0
a = []
while True:
    a.append(checkInputData())
    if a[i] == 0:
        break
    i += 1
del a[len(a) - 1]
a = sorted(a)
print(a[len(a)-2])
