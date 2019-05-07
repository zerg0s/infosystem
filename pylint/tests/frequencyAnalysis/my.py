f = open('input.txt', 'r', encoding='UTF-8')
words = {}
for i in f.read().split():
    words[i] = words.get(i, 0) - 1
sortedWords = sorted(zip(words.values(), words.keys()))
print(*(sortedWords[i][1] for i in range(len(sortedWords))), sep='\n')
