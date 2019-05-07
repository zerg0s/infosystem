def rec():
    numbers = int(input())
    if numbers != 0:
        rec()
    print(numbers)
rec()
