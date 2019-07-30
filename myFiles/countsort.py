# Created by Anita Kuzmina
# count_sort
# 23.10.2018


def CountSort(A):
    minCount = 0
    maxCount = 100
    count = [0] * (maxCount - minCount + 1)

    for i in A:
        count[i - minCount] += 1

    result = []
    for j in range(minCount, maxCount + 1):
        result += [j] * count[j]
    return result


lst = [int(i) for i in input("Enter sequence: ").split()]
print(' '.join(str(n) for n in CountSort(lst)))
