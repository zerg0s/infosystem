lst = input().split()
for i in reversed(range(len(lst))):
    if lst[i] == '0':
        lst.append(lst.pop(i))
print(*lst)