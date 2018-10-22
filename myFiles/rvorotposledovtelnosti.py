def rec():
    N = int(input())
    if N != 0:
        rec()
    print(N)
rec()
