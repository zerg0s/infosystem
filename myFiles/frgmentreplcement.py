#Created by Grebneva Kseniya
#fragment_replacement
#05.10.2018

s = str(input("Введите строку: "))
repl = s[(s.find('h') + 1) : s.rfind('h')]
repl = repl.replace('h','H')
print(s[0:s.find('h') + 1] + repl + s[s.rfind('h'):])
