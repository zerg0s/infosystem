# Created by Mikhail Fadeev
# Task Description: Выборы Государственной Думы

parties = {}
totalVotes = 0
file = open('input.txt', 'r', encoding='utf-8')
for line in file.readlines():
    partyName = line[0:line.rfind(" ")]
    numberVotes = int(line[line.rfind(" ") + 1:])
    parties.setdefault(partyName, numberVotes)
    totalVotes += numberVotes
file.close()

firstSelectiveQuotient = totalVotes / 450

parliamentSeats = {}

remainingVoices = []

distributedSeats = 0
for partyName, partyVotes in parties.items():
    distributedValue = partyVotes / firstSelectiveQuotient
    seatsAmount = int(distributedValue)
    remainingValue = distributedValue - seatsAmount

    parliamentSeats.setdefault(partyName, seatsAmount)
    distributedSeats += seatsAmount

    remainingVoices.append((partyName, remainingValue))

if distributedSeats < 450:
    for remainingVoice in sorted(remainingVoices,\
                                 key=lambda voices: voices[1], reverse=True):
        parliamentSeats[remainingVoice[0]] += 1
        distributedSeats += 1
        if distributedSeats == 450:
            break

for parliamentSeat in parliamentSeats.items():
    print(parliamentSeat[0] + " " + str(parliamentSeat[1]))
