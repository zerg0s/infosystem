#Исхаков Дамир
#Сложение без сложения
#27.09.2018
def summa(an, bn):
    if an == 0:
     return bn
     return summa(an-1, bn+1)

