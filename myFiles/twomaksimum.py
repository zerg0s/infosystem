#Created by Olesya Bandurina
#Date 20.09.2018
#Task Description: Определите значение второго по величине элемента в этой последовательности

max1 = int(input())
max2 = int(input())
if max2 > max1:
     max1, max2 = max2, max1
while max2 != 0:
    t = int(input())
    if t == 0:
        break
    if t > max1:
        max1, max2 = t, max1
    elif t > max2:
        max2 = t
print(max2)

