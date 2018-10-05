# Created by Samohin Artem
# Date 2018-09-16
# Task Description: http://www.hostedredmine.com/issues/773477

# Функция check_input() служит для проверки входных данных


def check_input():
    in_data = input()
    if in_data.lstrip("-").isdigit():
        data = int(in_data)
        return data
    else:
        print("Недопустимый ввод! " + "'" + in_data +
              "'" + " не является целым числом!")
        return exit(0)


# Функция input_data() служит для получения входных данных


def input_data():
    index = 0
    value_list = list()
    while(1):
        value_list.insert(index, check_input())
        if int(value_list[index]) == int(0):
            break
        index += 1
    if len(value_list) < 6:
        print("0")
        exit(0)
    return [int(item) for item in value_list]


my_list = input_data()
i = 1  # индекс
left = int(0)  # координаты первого локального минимума
right = int(0)  # координаты второго локального минимума
local_min = int(0)  # значение минимального пути
while int(my_list[i+1]) != 0:
    if(int(my_list[i]) > int(my_list[i-1])) \
       and (int(my_list[i]) > int(my_list[i+1])):
        if left == 0:
            left = i
            i = i + 1
            continue
        if right == 0:
            right = i
        if(left != 0) and (right != 0):
            if (local_min >= right - left) or (local_min == 0):
                local_min = right - left
                left = right
                right = 0
    i = i + 1
print(local_min)
