s1 = input()
s2 = s1.find("h")
sLast = s1.rfind("h")
print(s1[:s2 + 1] + s1[s2 + 1:sLast].replace("h", "H") + s1[sLast:])
