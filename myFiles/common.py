#Created by Petr Gusev
#Count of common pars
#16.10.2018

lst1 = input("Введите числа через пробел: ").split()
print(lst1)
count = 0

for i in range(len(lst1) - 1):
    for j in range(i+1, len(lst1)):
        if int(lst1[i]) == int(lst1[j]):
            count += 1

print(count)
