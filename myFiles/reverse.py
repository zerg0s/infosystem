def reverse():
    print('Введите число:')
    InputNumber = int(input())
    if InputNumber != 0:
        reverse()
    print(InputNumber)
reverse()
