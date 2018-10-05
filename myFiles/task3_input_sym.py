# Created by Samohin Artem
# Date 2018-09-24
# Task Description: http://www.hostedredmine.com/issues/775305

a = input()
b = ""
for i in range(0, len(a)-1):
    b = b + a[i] + "*"

b = b + a[len(a) - 1]
print(b)
