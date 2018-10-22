# Ильдар Галиуллин.
# Количество совпадающих пар.
# 08.10.2018.

list1 = [int(s) for s in input().split()]
j = 1
count = 0
for i in range(len(list1)):
    for j in range(i + 1, len(list1)):
        if list1[i] == list1[j]:
            count += 1
print(count)
