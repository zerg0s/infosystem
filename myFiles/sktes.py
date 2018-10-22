# Ильдар Галиуллин.
# Коньки.
# 21.10.2018.

skateSize = [int(s) for s in input().split()]
legSize = [int(s) for s in input().split()]
weared = 0
for i in range(len(legSize)):
    for j in range(len(skateSize)):
        if legSize[i] == skateSize[j]:
            skateSize.pop(j)
            j -= 1
            weared += 1
            break
for i in range(len(legSize)):
    for j in range(len(skateSize)):
        if legSize[i] < skateSize[j]:
            skateSize.pop(j)
            j -= 1
            weared += 1
            break
print(weared)
