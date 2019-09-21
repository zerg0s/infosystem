x1 = int(input('Введите координату начала 1 спички: '))
x2 = int(input('Введите координату конца 1 спички: '))
x3 = int(input('Введите координату начала 2 спички: '))
x4 = int(input('Введите координату конца 2 спички: '))
x5 = int(input('Введите координату начала 3 спички: '))
x6 = int(input('Введите координату конца 3 спички: '))

L1 = x2 - x1
L2 = x4 - x3
L3 = x6 - x5
num = "123"

while (x5 < x3 or x3 < x1):
    if x3 < x1:
        tmpx3 = x3
        tmpx4 = x4
        x3 = x1
        x4 = x2
        x1 = tmpx3
        x2 = tmpx4
        L1 = x2 - x1
        L2 = x4 - x3
        num = num[1] + num[0] + num[2]
    if x5 < x3:
        tmpx5 = x5
        tmpx6 = x6
        x5 = x3
        x6 = x4
        x3 = tmpx5
        x4 = tmpx6
        L3 = x6 - x5
        L2 = x4 - x3
        num = num[0] + num[2] + num[1]
    if x5 < x1:
        tmpx5 = x5
        tmpx6 = x6
        x5 = x1
        x6 = x2
        x1 = tmpx5
        x2 = tmpx6
        L3 = x6 - x5
        L1 = x2 - x1
        num = num[2] + num[1] + num[0]
if x3 <= x2 and x3 >= x1 and x4 >= x5 and x4 <= x6:
    print('0')
    exit()
if x5 - x4 <= L1:
    #print('1')
    print(num[0])
    exit()
elif x5 - x2 <= L2:
    #print('2')
    print(num[1])
    exit()
elif x3 - x2 <= L3:
    #print('3')
    print(num[2])
    exit()
if x5 - x4 <= L1:
    #print('1')
    print(num[0])
    exit()
elif x3 - x2 <= L3:
    #print('3')
    print(num[2])
    exit()
else:
    print('-1')
    exit()
