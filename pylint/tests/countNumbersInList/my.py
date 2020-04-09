lst = [0] * 9
a = int(input())
while a != 0:
    lst[a - 1] += 1
    a = int(input())
for i in lst:
    print(i, end=" ")
