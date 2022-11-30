import sys
tekst =  sys.stdin.readline().strip()

prefix = ""
sufix = ""
tulemus = ""
for s in tekst:
    if s == "[":
        sufix = prefix + tulemus + sufix
        prefix = ""
        tulemus = ""
    elif s == "]":
        prefix = prefix + tulemus + sufix
        sufix = ""
        tulemus = ""
    else:
        tulemus += s
tulemus = prefix + tulemus + sufix
print(tulemus)

