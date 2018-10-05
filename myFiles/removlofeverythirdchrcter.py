#Created by Grebneva Kseniya
#removal_of_every_third_character
#05.10.2018

s = list(input("Введите строку: "))
del s[::3]
print(''.join(s))
