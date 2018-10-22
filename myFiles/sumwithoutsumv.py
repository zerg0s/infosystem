# Created by Anita Kuzmina
# sum_without_sum
# 30.09.2018


def countSumWithoutSum(firstNum, secondNum):
    if firstNum == 0:
        return secondNum
    return countSumWithoutSum(firstNum - 1, secondNum + 1)


firstNumber = int(input("Enter first number: "))
secondNumber = int(input("Enter second number: "))
print("Sum: ", countSumWithoutSum(firstNumber, secondNumber))
