number, count = map(int, input().split())
allItems = list(map(int, input().split()))
center = number // 2
for i in range(len(allItems)):
    if allItems[i] == center and number % 2 == 1:
        print(allItems[i])
        break
    elif allItems[i] >= center:
        print(allItems[i - 1], allItems[i])
        break
