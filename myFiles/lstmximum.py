# Created by Anita Kuzmina
# last_maximum
# 23.10.2018

lst = input("Enter sequence: ").split()
maxEl = lst[0]
index = 0

for i in range(len(lst)):
    if lst[i] >= maxEl:
        maxEl = lst[i]
        index = i

print("Result: ", maxEl, index)
