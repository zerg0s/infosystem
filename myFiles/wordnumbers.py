# Created by Fedyuk Yuliya
# wordNumbers
# 09.11.2018
Words = ''
counter = {}
f = open('input.txt', 'r')
for line in f:
    Words = Words + ' ' + line.replace('\n', '')
f.close()
for word in Words.split():
    counter[word] = counter.get(word, 0) + 1
    print(counter[word] - 1, end=' ')
