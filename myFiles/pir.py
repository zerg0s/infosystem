# Аверина Мария
# Количество совпадающих пар
# 19.10.2018


lst = list(map(int, input("Введите список чисел: ").split()))
print(sum(lst.count(x) - 1 for x in lst) // 2)
