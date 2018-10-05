a = int(input("Введите а: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))
d = int(input("Введите d: "))

if(a==0):
    print("INF")
else:
    if((-b/a) == (-d/c)):
        print("NO")
    else:
        print(int(-b/a))

