l1 = int(input("Введите координату левого конца первой спички: "))
r1 = int(input("Введите координату правого конца первой спички: "))
l2 = int(input("Введите координату левого конца второй спички: "))
r2 = int(input("Введите координату правого конца второй спички: "))
l3 = int(input("Введите координату левого конца третьей спички: "))
r3 = int(input("Введите координату правого конца третьей спички: "))

if (l2 <= r1 and l3 <= r2 and l1 <= l2 and l2 <= l3)\
    or (l3 <= r1 and l2 <= r3 and l1 <= l3 and l3 <= l2)\
    or (l1 <= r2 and l3 <= r1 and l2 <= l1 and l1 <= l3)\
    or (l3 <= r2 and l1 <= r3 and l2 <= l3 and l3 <= l1)\
    or (l2 <= r3 and l1 <= r2 and l3 <= l2 and l2 <= l1)\
        or (l1 <= r3 and l2 <= r1 and l3 <= l1 and l1 <= l2):
        print(0)
elif (l2 - r3 >= 0 and l2 - r3 <= r1 - l1)\
        or (l3 - r2 >= 0 and l3 - r2 <= r1 - l1)\
        or (r1 - l1 > l2 - r1) or (r1 - l1 > l3 - r1)\
        or (r1 - l1 > l1 - r2) or (r1 - l1 > l1 - r3):
        print(1)
elif (l3 - r1 >= 0 and l3 - r1 <= r2 - l2)\
        or (l1 - r3 >= 0 and l3 - r1 <= r2 - l2)\
        or (r2 - l2 > l1 - r2) or (r2 - l2 > l3 - r2)\
        or (r2 - l2 > l2 - r1) or (r2 - l2 > l2 - r3):
        print(2)
elif (l2 - r1 >= 0 and l2 - r1 <= r3 - l3)\
        or (l1 - r2 >= 0 and l1 - r2 <= r3 - l3)\
        or (r3 - l3 > l1 - r3) or (r3 - l3 > l2 - r3)\
        or (r3 - l3 > l3 - r1) or (r3 - l3 > l3 - r2):
        print(3)
else:
    print(-1)
