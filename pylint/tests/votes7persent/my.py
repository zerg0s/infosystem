
def readIntList():
    return list(map(int, input().split()))


def readInt():
    return int(input())


def readIntN(n):
    return [int(input()) for i in range(n)]


def readListN(n):
    return [input().split() for i in range(n)]


def main():
    res, votes = [], []
    fl = False
    it = 0
    for line in open('input.txt', 'r', encoding='utf-8'):
        if line == 'PARTIES:\n':
            continue
        if line == 'VOTES:\n':
            fl = True
            res.sort()
        elif fl:
            votes.append(line)
        else:
            it += 1
            res.append([line, it, 0])
    votes.sort()
    it, threshold = 0, len(votes) * 0.07
    for elem in votes:
        while elem != res[it][0]:
            it += 1
        res[it][2] += 1
    res.sort(key=lambda x: (-x[2], x[0]))
    for elem in res:
        print(elem[0], end='')

if __name__ == '__main__':
    main()