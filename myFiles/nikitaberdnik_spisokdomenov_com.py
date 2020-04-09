import re

c = input('Строка:')
r = re.findall(r'\.\w\w\w?\.\w\w\w?|@\w+\.\w\w\w?[^.,]\b', c) + re.findall(r'\.\w\w\w?[^.]|\.\w\w\w?\Z', c)
d = []
for dom in r:
    d.append(re.sub(r'^[.@]|[.,"]$', '', dom))

for dom in d:
    print(dom)
#r'(@(\w+)?(\.\w+)?(\.\w+)?(\.\w+)?)'