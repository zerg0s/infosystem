# Автор: Ира Данилова
# Задача: Сумма без суммы

def sum(numberOne, numberTwo):
    if numberTwo != 0:
        return sum(numberOne + 1, numberTwo - 1)
    else:
        return numberOne

valueOne = int(input())
valueTwo = int(input())

print(sum(valueOne, valueTwo))
