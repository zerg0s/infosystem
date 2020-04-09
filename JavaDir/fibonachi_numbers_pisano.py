def calcFib(k):
    fib1 = 0
    fib2 = 1
    if k == 0:
        return 0
    i = 1
    while i < k:
        fib1, fib2 = fib2, fib1 + fib2
        i += 1
    return fib2


def getPisano(m):
    if m <= 1:
        return m
    periodLength = 1
    i = 1
    while True:
        currentdigit = calcFib(i) % m
        nextDigit = calcFib(i + 1) % m
        if (currentdigit == 0 and nextDigit == 1):
            break
        periodLength += 1
        i += 1
    return periodLength


if __name__ == "__main__":
    fibNum, m = map(int, input().split())
    print(calcFib(fibNum % getPisano(m)) % m)
    # for n in range(99):
    #     print(f"{calc_fib(n) % 10}    {calc_fib2(n)}")
