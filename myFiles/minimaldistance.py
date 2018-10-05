#Created by Olesya Bandurina
#Date 20.09.2018
#Task Description: Определите наименьшее расстояние между двумя локальными максимумами

i = 0
c1 = 1
c2 = 0
c3 = 0
m1 = 0
m2 = 0
r = 10000
while c1 != 0:
    i += 1
    c3 = c2
    c2 = c1
    c1 = int(input("введите последовательность целых чисел, для окончания введите ноль: "))
    if (i > 2) and (c2 > c1) and (c2 > c3) and (c1 != 0):
        m2 = m1
        m1 = i
    if (m1 > 0) and (m2 > 0) and (m1 - m2 < r):
            r = m1- m2
if r == 10000:
    r = 0
print(r)
