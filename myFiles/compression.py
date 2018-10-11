# Ильдар Галиуллин.
# Сжатие списка.
# 08.10.2018.

count = 0
numbers = [int(s) for s in input().split()]
for i in range(len(numbers)):
    j = i - count
    if numbers[j] == 0:
        numbers.append(numbers.pop(j))
        count += 1
print(numbers)
