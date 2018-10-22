# Created  by Maltsev Alexey
# 16.10.18
# Количество совпадающих пар

num = list(map(int, input("Введите числа: ").split()))
pair = 0
for i in num:
    for j in num:
        if i == j:
            pair = pair + 1
    pair = pair - 1
pair = pair // 2
print("Количество совпадающих пар:  ", pair)
