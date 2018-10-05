#Created by Grebneva Kseniya
#complex_equation
#14.09.2018

print('(ax+b)/(cx+d) = 0')

A = int(input("a = "))
B = int(input("b = "))
C = int(input("c = "))
D = int(input("d = "))

if(((C == 0) and (D == 0)) or ((A == 0) and (B != 0)) or ((B/A) == (D/C))):
    print('NO')
elif((A == 0) and (B == 0)):
    print('INF')
else:
    X = int(-B/A)
    if(X != 0):
        print('x =', X)
    else:
        print('NO')
