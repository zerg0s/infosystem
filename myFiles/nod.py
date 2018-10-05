# Created by Samohin Artem
# Date 2018-09-28
# Task Description: http://www.hostedredmine.com/issues/775916

# check float
def checkInput():
    inData = input()
    try:
        data = float(inData)
    except ValueError:
        print("Неверный ввод! Координата должна быть действительным числом!")
        exit(0)
    return data


def nodCreate(a, b):
    if a!=0 and b!=0:
        if a > b:
            a = a % b
            nod(a, b)
        else:
            b = b % a
            nod(a, b)
    else:
        print(str(a+b))

X = checkInput()
Y = checkInput()

nodCreate(X, Y)