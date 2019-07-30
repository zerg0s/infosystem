# Ильдар Галиуллин.
# Гражданская оборона.
# 21.10.2018.

townsCount = int(input())
townsDist = [int(s) for s in input().split()]
bombCount = int(input())
bombDist = [int(s) for s in input().split()]
safeBomb = []
series = []
for i in range(len(townsDist)):
    series.append(i + 1)
for i in range(len(townsDist)):
    townBombDiff = []
    for j in range(len(bombDist)):
        townBombDiff.append(abs(townsDist[i] - bombDist[j]))
    townBombDiffSeries = zip(townBombDiff, series)
    tbds = sorted(townBombDiffSeries, key=lambda tup: tup[0])
    safeBomb.append([townBombDiffSeries[1] for townBombDiffSeries in tbds][0])
for i in safeBomb:
    print(i, end=' ')
