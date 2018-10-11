# Created by Olesya Bandurina
# Date 9.10.2018
# Task Description: определите количество списке элементов, которые больше двух своих соседей

a = input().split()
m = 0
for i in range(1, len(a)-1):
    if int(a[i-1]) < int(a[i]) and int(a[i]) > int(a[i+1]):
        m += 1
print(m)

