# Created by Fedyuk Yuliya
# biggerThanNeighbors
# 19.10.2018
print("Введите список чисел: ")
listik = [int(s) for s in input().split()]
count = 0
for i in range(1, len(listik) - 1):
    if listik[i] > listik[i - 1] and listik[i] > listik[i + 1]:
        count += 1
print("Количество элементов, больших двух своих соседей, равняется: ", count)
