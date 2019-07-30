# Ильдар Галиуллин.
# Наименьший нечетный.
# 18.11.2018.


def oddNum(x):
    if x % 2 == 0:
        return 0
    else:
        return 1


print(min(filter(oddNum, map(int, input().split()))))
