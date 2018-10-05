# Created by Anita Kuzmina
# euclidean_algorithm
# 28.09.2018


def gcd(firstNumber, secondNumber):
    return abs(firstNumber) if secondNumber == 0 else gcd(secondNumber, firstNumber % secondNumber)


firstNum = int(input("Enter first number: "))
secondNum = int(input("Enter second number: "))

print("Greatest common divisor: ", gcd(firstNum, secondNum))
