# Аверина Мария
# Разворот последовательности
# 12.10.2018


def rec():
    num = int(input())
    if num != 0:
        rec()
    print(num)


rec()
