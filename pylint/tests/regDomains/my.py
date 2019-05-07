# Created by Samohin Artem
# Date 2019-12-21
# Task Description: http://www.hostedredmine.com/issues/803176
# Необходимо с помощью регулярных выражений вернуть список доменов 1 и 2 уровня(если есть) из списка адресов электронной почты, заданного строкой через "," 
#Пример:
#Ввод:
#"myMail@gmail.com, company@xerox.co.uk" 
#Вывод:
#com
#gmail.com
#uk
#co

import re

emailList = list(input().split(","))
for i in range(0, len(emailList)):
    if re.compile('(\S+)([.]||[@])(\w+)[.](\w+)$').match(emailList[i].replace(" ", "")) is not None:
        print("\n".join(str(x) for x in
                        reversed(re.search('([.]||[@])(\w+)[.](\w+)$',
                                           emailList[i].replace(" ", "")).group()[1:].split("."))))
