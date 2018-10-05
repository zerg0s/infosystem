# Created by Fedyuk Yuliya
# PerfectPerformer
# 25.09.2018


def checkInput():
    in_data = input()
    if in_data.isdigit():
        data = int(in_data)
        return data
    print("Недопустимый ввод! " + "'" + in_data +
          "'" + " не является натуральным числом!")
    return exit(0)


print("Введите число, которое необходимо уменьшить: ")
bNum = checkInput()
print("Введите число, которео должно получиться: ")
fNum = checkInput()
if bNum > fNum:
    while bNum != fNum:
        if(bNum/2 - fNum > 0) and (bNum % 2 == 0):
            bNum = bNum/2
            print(":2")
        if (bNum/2 - fNum < 0) or (bNum % 2 != 0) or (bNum - fNum == 1):
            bNum = bNum - 1
            print("-1")
else:
    exit(0)
input()
