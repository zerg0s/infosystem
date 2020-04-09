dip = list(map(int, input().strip().split()))
count = list(map(int, input().strip().split()))

for i in range(dip[0], dip[1]+1):
    for j in range(count[0], count[1]+1):
        print(i, 'x', j, '=', i*j)
    print()