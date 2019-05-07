a = int(input())
count = [0] * 9
while a != 0:
    count[a - 1] += 1
    a = int(input())
print(*count)
