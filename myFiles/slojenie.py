def sum(a, b):
    if a == 0:
        return b;
    return sum(a-1, b+1)
