# Created by Alexey Maltsev
# 25.09.18
# Вставка символа

stroka = input("Введите строку :")
p = ""
i = 0
d = len(stroka)
while i < d:
    if i > 0:
        p = p + "*"
    p = p + stroka[i]
    i = i + 1
print(p)
