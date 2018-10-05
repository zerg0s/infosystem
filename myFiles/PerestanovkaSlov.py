s = input("Введите строку: ")
n = s.find(" ")
new = s[n+1:]+s[n:n+1]+s[:n]
print(new)
