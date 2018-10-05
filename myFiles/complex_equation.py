#Created by Grebneva Kseniya
#complex_equation
#14.09.2018

print('(ax+b)/(cx+d) = 0')
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
d = int(input("d = "))
if(((c==0) and (d==0)) or ((a==0) and (b!=0)) or ((b/a)==(d/c))):
    print('NO')
elif((a==0) and (b==0)):
    print('INF')
else:
    x = int(-b/a)
    if(x != 0):
        print('x =',x)
    else:
        print('NO')
