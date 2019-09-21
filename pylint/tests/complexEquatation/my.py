a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a == 0:
    if b == 0:
        print('INF')
    else:
        print('NO')
elif b % a != 0:
    print('NO')
else:
    x = -b // a
    if c*x + d == 0:
        print('NO')
    else:
        print(x)
