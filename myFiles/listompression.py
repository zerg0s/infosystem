# Created by Fedyuk Yuliya
# listСompression
# 19.10.2018

print("Введите целые числа: ")
count = 0
numbers = [int(i) for i in input().split()]
for j in range(len(numbers)):
    k = j - count
    if numbers[k] == 0:
        numbers.append(numbers.pop(k))
        count += 1
print("Новый список", numbers)
