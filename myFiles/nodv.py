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


def nodCreate(inA, inB):
    if inA != 0 and inB != 0:
        if inA > inB:
            inA = inA % inB
            nodCreate(inA, inB)
        else:
            inB = inB % inA
            nodCreate(inA, inB)
    else:
        print(str(inA+inB))


X = checkInput()
Y = checkInput()
nodCreate(X, Y)
