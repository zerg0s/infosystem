# Аверина Мария
# Расписание звонков
# 20.10.2018


num = int(input("Введите номер урока: "))
num1 = num - 1

time1 = (num1 // 2 * 20) + (num1 % 2) * 5
lesson = num * 45
time = time1 + lesson
hours = time // 60
minute = time % 60

print(hours + 9, minute)
