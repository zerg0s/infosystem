# Created by Anita Kuzmina
# best_neighbor
# 09.10.2018

lst = input("Enter sequence: ").split()
count = 0

for i in range(1, len(lst)-1):
    if lst[i] > lst[i - 1] and lst[i] > lst[i + 1]:
        count += 1

print("Number of elements bigger than it's neighbors: ", count)
