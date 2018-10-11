# Created by Anita Kuzmina
# even_indexes
# 09.10.2018

lst = input("Enter sequence: ").split()
evenLst = []

for i in range(len(lst)):
    if i % 2 == 0:
        lst.append(evenLst[i])

print("Sequence of even elements: ", evenLst)
