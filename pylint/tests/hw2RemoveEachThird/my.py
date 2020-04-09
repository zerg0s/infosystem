s1 = input()
i = 0
res = ""
while i < len(s1):
    if i % 3:
        res += s1[i]
    i += 1
print(res)
