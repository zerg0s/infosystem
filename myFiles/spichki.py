#Исхаков Дамир
#Спички
#19.09.2018
l1 = int(input("Введите, пожалуйста, координаты первой спички: "))
r1 = int(input("Введите, пожалуйста, координаты первой спички: "))
l2 = int(input("Введите, пожалуйста, координаты второй спички: "))
r2 = int(input("Введите, пожалуйста, координаты второй спички: "))
l3 = int(input("Введите, пожалуйста, координаты третьей спички: "))
r3 = int(input("Введите, пожалуйста, координаты третьей спички: "))
if 0 <= l1 < r1 <= 100 and 0 <= l2 < r2 <= 100 and 0 <= l3 < r3 <= 100:
    if (l1 <= r2 and l2 <= r1 and l2 <= r3 and l3 <= r2)\
            or (l2 <= r1 and l1 <= r2 and l1 <= r3 and l3 <= r1)\
            or (l2 <= r3 and l3 <= r2 and l3 <= r1 and l1 <= r3)\
            or (l3 <= r2 and l2 <= r3 and l2 <= r1 and l1 <= r2)\
            or (l3 <= r1 and l1 <= r3 and l1 <= r2 and l2 <= r1)\
            or (l1 <= r2 and l3 <= r1 and l3 <= r2 and l2 <= r3):
        print(0)
    else:
        f1 = r1 - l1
        f2 = r2 - l2
        f3 = r3 - l3
        if (l3 > r2 and f1 >= l3 - r2)\
                or (l2 > r3 and f1 >= l2 - r3)\
                or (l2 <= r3 and l3 <= r2):
            print(1)
        elif (l3 > r1 and f2 >= l3 - r1)\
                or (l1 > r3 and f2 >= l1 - r3)\
                or (l1 <= r3 and l3 <= r1):
            print(2)
        elif (l1 > r2 and f3 >= l1 - r2)\
                or (l2 > r1 and f3 >= l2 - r1)\
                or (l1 <= r2 and l2 <= r1):
            print(3)
        else:
            print(-1)
else:
    print(-1)
