def calcFib(k):
    fib1 = 0
    fib2 = 1
    if k == 0:
        return 0
    i = 1
    while i < k:
        fib1, fib2 = fib2, (fib1 + fib2)
        i += 1
    return fib2


if __name__ == "__main__":
    # for fibNum in range(10):
    #     print(calcFib(fibNum), end=" ")
    # print()
    #
    # for i in range(100):
    #     temp = 0
    #     for fibNum in range(i + 1):
    #         temp += calcFib(fibNum)
    #     print(temp % 10, end=" ")
    # print()

    fibNum = int(input())
    # for fibNum in range(100):
    if fibNum <= 2:
        print(fibNum, end=" ")
    else:
        print((calcFib((fibNum + 2) % 60) - 1) % 10, end=" ")
