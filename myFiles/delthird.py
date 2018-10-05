# Created by Alexey Maltsev
# 24.09.18
# Удаление каждого третьего

stroka = input("Введите строку :")
res = ""
i = 0
while i <= len(stroka):
    if i % 3 != 0:
        res = res + stroka[i]
    i = i + 1
print(res)
