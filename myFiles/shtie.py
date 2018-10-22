#Исхаков Дамир
#"Сжатие" списка
#15.10.2018
a = input().split()
b = [x for x in a if x != '0']
b.extend(x for x in a if x == '0')
print(' '.join(b))
