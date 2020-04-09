def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


if __name__ == "__main__":
    x, y = map(int, input().split())
    print(gcd(x, y))
