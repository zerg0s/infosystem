#Created by Petr Gusev
#8 Queens not attack anybody
#19.10.2018



x = []
y = []

for i in range(8):
    forX, forY = [int(s) for s in input().split()]
    x.append(forX)
    y.append(forY)

booly = False

for i in range(8):
    for j in range(i + 1, 8):
        if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
            booly = True

if booly:
    print("YES")
else:
    print("NO")
