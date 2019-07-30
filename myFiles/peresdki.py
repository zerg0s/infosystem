a = int(input())
b = int(input())
n = int(input())
for num in range(a, b+1):
    sum = 0
    t = num
    while t > 0:
        sum += t % 10
        t /= 10
    if sum == n:
        print(num)
