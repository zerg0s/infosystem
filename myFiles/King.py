a = int(input())
b = int(input())
c = int(input())
d = int(input())
k =(a - c)**2 + (b - d)**2

if (k <= (a - c)**2 + (b - d)**2 <= 2):
    print('YES')

else:
    print ('NO')
