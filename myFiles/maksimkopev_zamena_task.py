import re

text = input()
regexp = r'(?<!\\)\*([\w\\*]+[^\\])\*'
print(re.sub(r'\\\*', r'*', re.sub(regexp, r'<b>\1</b>', text)))
