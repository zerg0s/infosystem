# Author: Danilova Irina
# Task: Desks

startH, startM = 9, 0
break1 = 5
break2 = 15
lesson = 45
lessonNumber = int(input("Введите номер урока: "))
end = lessonNumber * lesson + (((lessonNumber) // 2) * break1) + (((lessonNumber - 1) // 2) * break2)
(dh, dm) = divmod(end,60)
print (startH + dh, startM + dm)

