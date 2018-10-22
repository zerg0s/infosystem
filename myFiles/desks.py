# Аверина Мария
# Расписание звонков
# 20.10.2018


import math

num1 = int(input())
num2 = int(input())
num3 = int(input())
desk = math.ceil((num1 + num2 + num3) / 2)
if int(desk / 3) > 1 or desk == 0:
    res = desk
else:
    res = desk + 1

print(res)
