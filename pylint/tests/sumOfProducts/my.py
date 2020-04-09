n = int(input())

sum = 0
for i in range(2, n + 1):
    print(f"{i - 1}*{i}", end="")
    sum += i * (i - 1)
    if i == n:
        print("=", end="")
    else:
        print("+", end="")
print(sum)