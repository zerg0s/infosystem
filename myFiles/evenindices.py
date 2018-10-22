# Created by Fedyuk Yuliya
# evenIndices
# 18.10.2018

print("Введите числа: ")
numbers = [int(f) for f in input().split()]
for i in range(len(numbers)):
    if i % 2 == 0:
        print('%d' % numbers[i], end=' ')

