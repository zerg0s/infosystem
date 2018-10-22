# Фадеев Михаил
# Расписание звонков

lessonNumber = int(input())

startTimeMin = 9 * 60
endTimeMin = startTimeMin + (45 * lessonNumber) + (5 * (lessonNumber - 1)) +\
             (10 * ((lessonNumber - 1) // 2))

print(str(endTimeMin // 60) + " " + str(endTimeMin % 60))
