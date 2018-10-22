#Created by Petr Gusev
#Change list 
#19.10.2018

lst1 = input("Введите числа через пробел: ").split()
count = 0

for i in range(len(lst1)):
    com = i - count
    if lst1[com] == '0':
        lst1.append(lst1.pop(com))
        count += 1

print(lst1)
