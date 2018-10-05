# Created by Samohin Artem
# Date 2018-09-24
# Task Description: http://www.hostedredmine.com/issues/775283

a = input()
b = ""
for i in range(0, len(a)):
    if i%3 != 0:
        b = b + a[i]
print(b)