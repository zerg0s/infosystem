# Created by Samohin Artem
# Date 2018-09-19
# Task Description: http://www.hostedredmine.com/issues/773475


def check_input():
    in_data = input()
    if in_data.lstrip("-").isdigit():
        data = int(in_data)
        return data
    print("Недопустимый ввод! " + "'" + in_data +
          "'" + " не является целым числом!")
    return exit(0)


def input_data():
    mylist = list()
    i = 0
    while(1):
        mylist.insert(i, check_input())
        if int(mylist[i]) == int(0):
            break
        i += 1
    mylist.remove(0)  # delete 0 from list
    return [int(item) for item in mylist]


sequence = list()
print("Введите ряд целых чисел(0-конец ввода):")
sequence = input_data()
dif = 0
for i in range(len(sequence)):
    if (max(sequence) - sequence[i] <= dif or dif == 0) and \
       (max(sequence) - sequence[i] != 0):
        dif = max(sequence) - sequence[i]
        secondMin = sequence[i]
print(secondMin)
