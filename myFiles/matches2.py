# Аверина Мария
# Спички
# 12.09.2018

l1 = int(input("Введите координату левого конца первой спички: "))
r1 = int(input("Введите координату правого конца первой спички: "))
l2 = int(input("Введите координату левого конца второй спички: "))
r2 = int(input("Введите координату правого конца второй спички: "))
l3 = int(input("Введите координату левого конца третьей спички: "))
r3 = int(input("Введите координату правого конца третьей спички: "))

x = (l2-l1)*(l2-r1) <= 0 or (r2-l1)*(r2-r1) <= 0
y = (l3-l1)*(l3-r1) <= 0 or (r3-l1)*(r3-r1) <= 0
z = (l3-l2)*(l3-r2) <= 0 or (r3-l2)*(r3-r2) <= 0

if (y and z) or (x and z) or (x and y):
    print(0)
else:
    length1 = r1-l1
    length2 = r2-l2
    length3 = r3-l3
    if (l2 > r3 and l2-r3 <= length1) or (r2 < l3 and l3-r2 <= length1) or (r3 >= l2 and l3 <= r2):
        print(1)
    elif (l1 > r3 and l1-r3 <= length2) or (r1 < l3 and l3 - r1 <= length2) or (r3 >= l1 and l3 <= r1):
        print(2)
    elif (l1 > r2 and l1-r2 <= length3) or (r1 < l2 and l2-r1 <= length3) or (r2 >= l1 and l2 <= r1):
        print(3)
    else:
        print(-1)