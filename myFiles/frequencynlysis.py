# Created by Fedyuk Yuliya
# frequencyAnalysis
# 10.11.2018
from collections import defaultdict
file = open("input.txt", "r", encoding="utf-8")
words = defaultdict(int)
for line in file.readlines():
    for word in line.strip().split():
        words[word] += 1
point = defaultdict(list)
for word, port in words.items():
    point[port].append(word)
for port, words in sorted(point.items(), key=lambda x: x[0], reverse=True):
    for word in sorted(words):
        print(word)
