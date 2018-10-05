#Created by Petr Gusev
#King go
#09.09.2018

print("Введите координаты клетки, на которой стоит король")
kingVer = int(input("Координата по вертикали:"))
kingHor = int(input("Координата по горизонтали:"))

print("Введите координаты клетки, куда нужно переместить короля")
newVer = int(input("Координата по вертикали:"))
newHor = int(input("Координата по горизонтали:"))

#Проверяем вдруг ввели одинаковые координаты 
if kingVer == newVer and kingHor == newHor:
	print("Король остается на своем месте")
	exit(1)
	
if (kingVer + 1) >= newVer and (kingVer - 1) <= newVer and (kingHor + 1) >= newHor and (kingHor - 1) <= newHor:
	print("YES")
else: print ("NO")