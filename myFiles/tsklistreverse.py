# Created by Mikhail Fadeev
# Task Description: Разворот последовательности

def inputNum():
    num = int(input())
    if num != 0:
        inputNum()
    print(num)

inputNum()
