import re

inputText = "Ночь. Улица. Фонарь. Аптека. Бессмысленный и тусклый свет. Живи еще хоть четверть века, всё будет так, исхода нет."
#inputText = input("Input text lines: ");
wordParser = re.findall('[\w]+[.]', inputText)
for word in wordParser:
    print(word[0:len(word)-1])