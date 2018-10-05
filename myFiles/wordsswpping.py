#Created by Grebneva Kseniya
#words_swapping
#05.10.2018

s = str(input("Введите два слова: "))
first = ''
second = ''
lst = s.split(' ')
lst[0], lst[1] = lst[1], lst[0]
print(' '.join(lst))
