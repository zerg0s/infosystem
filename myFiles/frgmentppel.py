# Заокопный Андрей
# Обращение фрагмента
# 20.10.18
s = input()
s = s[:s.find('h') + 1] + s[s.rfind('h') - 1:s.find('h'):-1] + s[s.rfind('h'):]
print(s)
