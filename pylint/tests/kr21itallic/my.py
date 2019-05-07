# Замена
import re
text = input()
for value in re.findall(r"[^\\]?(\*.*?[^\\]\*)", text):
    text = text.replace(value, "<b>" + value.replace("\\*", "*")[1:-1]\
                        + "</b>")
print(text)