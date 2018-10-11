# Created by Anita Kuzmina
# list_compression
# 09.10.2018

lst = input("Enter sequence: ").split()
prevEl = 0

for i in range(len(lst)):
    if lst[i - prevEl] == '0':
        lst.append(lst.pop(i - prevEl))
        prevEl += 1

print("Compressed sequence: ", lst)
