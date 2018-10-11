# Ильдар Галиуллин.
# Больше соседей.
# 08.10.2018.

list1 = [int(s) for s in input().split()]
count = 0
for i in range(1, len(list1) - 1):
    if list1[i] > list1[i - 1] and list1[i] > list1[i + 1]:
        count += 1
print(count)
