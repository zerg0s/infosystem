# Created by Fedyuk Yuliya
# lastMax
# 23.10.2018
print("Введите значения: ")
listik = list(map(int, input().split()))
maximum = 0
count = 0
for i in range(len(listik) - 1, -1, -1):
    if maximum < listik[i]:
        maximum = listik[i]
        count = i
print(maximum, count)
