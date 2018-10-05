#Мария Евсеева
#Разворот последовательности

def InputNumber():
    number = int(input())
    if number == 0:
        print(number)
    else:
        InputNumber()
        print(number)

InputNumber()
