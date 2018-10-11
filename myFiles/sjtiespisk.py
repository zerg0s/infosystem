a = input().split()
for i in reversed(range(len(a))):
    if a[i] == '0':
        a.append(a.pop(i))
print(*a)
