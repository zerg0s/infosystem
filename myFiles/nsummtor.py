# Мальцев Алексей
# Контрольная работа 20.10.18
# Сумма десятичных цифр

res = 0
i = 0
number = int(input())
numberf = str(number)
dlen = len(numberf)
while i < dlen:
    res = int(numberf[i - 1]) + res
    i = i + 1
print(res)
