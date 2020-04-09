numb = int(input())

now = 1
ans = 0
for i in range(numb):
    now *= (i + 1)
    ans += now

print(ans)
