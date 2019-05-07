s = list(input().strip())
i = 1
reject = {'a', 'e', 'h', 'i', 'o', 'u', 'w', 'y'}
other = [set(),
         {'b', 'f', 'p', 'v'},
         {'c', 'g', 'j', 'k', 'q', 's', 'x', 'z'},
         {'d', 't'},
         {'l'},
         {'m', 'n'},
         {'r'}
        ]
while i < len(s):
    if s[i] in reject:
        s.pop(i)
    else:
        j = 1
        while s[i] not in other[j]:
            j += 1
        s[i] = str(j)
        if s[i] == s[i - 1]:
            s.pop(i)
        else:
            i += 1
print(*s[:4], '0' * max(0, 4 - len(s)), sep='')
