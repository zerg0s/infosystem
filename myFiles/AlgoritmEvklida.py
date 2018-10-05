def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

x = int(input())
y = int(input())
print(gcd(x, y))
