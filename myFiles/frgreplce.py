#Галиуллин Ильдар.
#Обращение фрагмента.
#20.10.18.

str1 = input()
str1 = str1[:str1.find('h') + 1] + \
       str1[str1.rfind('h') - 1:str1.find('h'):-1] + \
       str1[str1.rfind('h'):]
print(str1)
