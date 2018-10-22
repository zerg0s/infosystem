# Created by Anita Kuzmina
# sum_without_sum
# 30.09.2018


def count_sum_without_sum(first_num, second_num):
    if first_num == 0:
        return second_num
    else:
        return count_sum_without_sum(first_num - 1, second_num + 1)


firstNum = int(input("Enter first number: "))
secondNum = int(input("Enter second number: "))

print("Sum: ", count_sum_without_sum(firstNum, secondNum))
