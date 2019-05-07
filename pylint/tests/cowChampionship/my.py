n = int(input())
participantsScores = list(map(int, input().split()))
winner = max(participantsScores)
winnerPos = participantsScores.index(winner)
vasilScore = -1
for i in range(1, n - 1):
    if winnerPos < i and participantsScores[i + 1] < participantsScores[i]:
        if participantsScores[i] % 10 == 5 and\
                        participantsScores[i] > vasilScore:
            vasilScore = participantsScores[i]
place = 1
if vasilScore == -1:
    print(0)
else:
    for element in participantsScores:
        if element > vasilScore:
            place += 1
    print(place)
