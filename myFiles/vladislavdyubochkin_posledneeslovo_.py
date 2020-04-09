import re
inputText = input("Input text lines: ");
wordParser = re.findall(r'\w+\.', inputText)
for word in wordParser:
    print(word[0:len(word)-1])
