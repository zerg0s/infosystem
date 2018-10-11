# Created by Anita Kuzmina
# matching_pairs
# 09.10.2018

lst = input("Enter sequence: ").split()
count = 0

for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] == lst[j]:
            count += 1

print("Number of matching pairs: ", count)
