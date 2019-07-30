statements = []
numbers = []
maxMatch = -1

for _ in range(int(input())):
    statements.append(set(input()))

for _ in range(int(input())):
    numbers.append((input()))

counter = [0 for _ in range(len(numbers))]

for i, num in enumerate(numbers):
    numSet = set(num)
    for statement in statements:
        if numSet >= statement:
            counter[i] += 1
    if counter[i] > maxMatch:
        maxMatch = counter[i]

for k, count in enumerate(counter):
    if count == maxMatch:
        print(numbers[k])
