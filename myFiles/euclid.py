# Автор: Ира Данилова
# Задача: Алгоритм Евклида

def gcd(valueOne, valueTwo):
    if valueOne == valueTwo:
        return valueOne
    elif valueOne > valueTwo:
        return gcd(valueOne - valueTwo, valueTwo)
    elif valueOne < valueTwo:
        return gcd(valueOne, valueTwo - valueOne)

firstNumber = int(input())
secondNumber = int(input())

print(gcd(firstNumber, secondNumber))
