#Created by Grebneva Kseniya
#jogging_in_the_morning
#21.09.2018

X = float(input("Введите пробег за первый день, x: "))
Y = float(input("Введите пробег за последний день, y: "))
C = 1

while(X <= Y):
    X += X*0.1
    C += 1
print("Номер дня, на который пробег составит не менее y км: ",C)
