#Заокопный Андрей
#Расписание звонков
#20.10.18

def lol():
	a = int(input())
	num_peremen = a - 1
	time_peremen = (num_peremen // 2 * 20) + (num_peremen % 2) * 5
	time_urok = a * 45
	
	time_all_minutes =  time_peremen + time_urok
	
	hours = time_all_minutes // 60 
	minutes = time_all_minutes % 60
	
	print(hours+9, minutes)