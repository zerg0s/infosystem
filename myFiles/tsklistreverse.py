# Created by Mikhail Fadeev
# Task Description: Разворот последовательности

def InputNum():
    num = int(input())
    if num != 0:
        InputNum()
    print(num)

InputNum()
