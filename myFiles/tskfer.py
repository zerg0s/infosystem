# Created by Samohin Artem
# Date 2018-10-07
# Task Description: http://www.hostedredmine.com/issues/777911

N = 8  # количество ферзей на доске

# Функция checkInput() служит для проверки входных данных


def checkInput():
    in_data = input()
    if in_data.isdigit():
        data = int(in_data)
        if data > 0 and data < N + 1:
            return data
    print("Недопустимый ввод! " + "'" + in_data +
          "'" + " не является числом от 1 до " + str(N) + "!")
    return exit(0)

mylist = list()
mainlist = list()
for i in range(1, N + 1):
    print("Введите координату x" + str(i) + ":")
    mylist.append(checkInput())
    print("Введите координату y" + str(i) + ":")
    mylist.append(checkInput())
    mainlist.append(mylist.copy())
    mylist.clear()

for i in range(0, N - 2):
    for j in range(0, N - 1):
        if abs(mainlist[i][0] - mainlist[j][0]) == abs(mainlist[i][1] - mainlist[j][1]) \
           and (abs(mainlist[i][0] - mainlist[j][0]) != 0 and abs(mainlist[i][1] - mainlist[j][1]) != 0):
            print("YES")
            exit(0)
print("NO")
