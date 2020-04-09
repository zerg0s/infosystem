import re

patt = re.compile(r"\\\*")
patt2 = re.compile(r"[*](.*?)[*]")
patt3 = re.compile(r"ekran")

rest1 = patt.sub("ekran", input())
rest2 = patt2.sub(r"<b>\1</b>", rest1)
rest3 = patt3.sub("*", rest2)
print(rest3)
