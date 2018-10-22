#Created by Grebneva Kseniya
#addition_without_addition
#15.10.2018

def res(a, b):
    if a == 0:
        return b
    else:
        return res(a - 1, b + 1)

firstNum = int(input('a = '))
secondNum = int(input('b = '))
res = res(firstNum, secondNum)
print(res)
