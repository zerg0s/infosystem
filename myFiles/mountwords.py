# Created by Fedyuk Yuliya
# amountWords
# 01.11.2018
import sys
firstFile = sys.stdin.read()
text = ''
for line in firstFile.readlines():
    text += line
amountWords = text.split()
print(amountWords)
print(len(amountWords))
