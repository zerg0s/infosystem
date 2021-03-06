def numberCheck(number):
    if number.lstrip('-+').isdigit() is not True:
        print('Данные введены неверно')
        exit()
    else:
        return int(number)


print(len({int(i) for i in map(numberCheck, input('Введите числа через пробел: ').split(" "))}))