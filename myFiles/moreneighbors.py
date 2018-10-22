# Аверина Мария
# Больше соседей
# 19.10.2018


lst = list(map(int, input("Введите список чисел: ").split()))
a = 0

for i in range(1, len(lst)-1):
    if lst[i-1] < lst[i] and lst[i] > lst[i+1]:
        a += 1

print(a)