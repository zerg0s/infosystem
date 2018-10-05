#Исхаков Дамир
#Сложение без сложения
#27.09.2018
def summa(a, b):
    if a == 0:
        return b;
    return summa(a-1, b+1)

