import re

def colourg(instr):
    patt = re.compile(r"(?:(?:#(\w)\1\1$)|(?:#(\w\w)\2\2$)|(?:rgb[(](\d+\.?\d+)\3\3[)])|(?:hsl[(]0,0%,\d+%[)]))")
    pattwb = re.compile(r"#fff|#ffffff|#000|#000000|rgb(0,0,0)|rgb(255,255,255)|hsl(0,0%,0%)|hsl(0,0%,100%)")
    instr = instr.replace(" ", "")
    instr = instr.lower()
    respat = patt.search(instr)
    if respat:
        respat2 = pattwb.search(instr)
        if not respat2:
            return "True"
        else:
            return "False"
    return "False"

print(colourg(input()))
