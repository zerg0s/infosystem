#Created by Petr Gusev
#More neighbors
#19.10.2018

a = input("Введите числа").split(" ")
count = 0

for i in range(1, len(a) - 1):
    if int(a[i-1]) < int(a[i]) > int(a[i+1]):
        count += 1

print(count)
