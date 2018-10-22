# Мария Евсеева
# Разворот последовательности

def inputNumber():
    number = int(input())
    if number == 0:
        print(number)
    else:
        inputNumber()
        print(number)

inputNumber()
