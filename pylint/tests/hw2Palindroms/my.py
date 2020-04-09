
def swapData(inData):
    newData = 0
    while inData > 0:
        lastDigit = inData % 10  # находим последнюю цифру
        inData = inData // 10  # убираем из числа последнюю цифру
        newData = newData * 10  # увеличиваем разрядность второго числа
        newData = newData + lastDigit  # добавили новую цифру
    return newData

k = int(input())
count = 0
for number in range(1, k + 1):
    if number == swapData(number):
        count += 1
print(count)
