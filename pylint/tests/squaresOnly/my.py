from math import sqrt

def reverseInput(count):
    number = int(input())
    if number == 0:
        if count == 0:
            print(0)
        return
    if sqrt(number).is_integer():
        reverseInput(1)
        print(number, end=' ')
    else:
        reverseInput(count)

reverseInput(0)
