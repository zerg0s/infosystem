n = int(input())
ans = [0] * n
settle = list(enumerate(map(int, input().split()), start=0))
m = int(input())
shelter = list(enumerate(map(int, input().split()), start=1))
settle.sort(key=lambda x: x[1])
shelter.sort(key=lambda x: x[1])
prev = 0
for i in range(n):
    now = prev
    while (now < m - 1 and abs(shelter[now][1] - settle[i][1]) >
            abs(shelter[now + 1][1] - settle[i][1])):
        now += 1
    prev = now
    ans[settle[i][0]] = shelter[now][0]
print(*ans)