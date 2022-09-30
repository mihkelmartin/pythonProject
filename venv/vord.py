import sys
s = sys.stdin.readline().split("?")
arv1 = int(s[0])
arv2 = int(s[1])
arv3 = int(s[2])
arv4 = int(s[3])

def teetehe(arv1, arv2, tehe):
    tulemus = 0
    if tehe == "+":
        tulemus = arv1 + arv2
    if tehe == "-":
        tulemus = arv1 - arv2
    if tehe == "*":
        tulemus = arv1 * arv2
    return tulemus


tehted = ["+", "-", "+"]

# vordusmärk 1  + +, + -, - +, - -, * +, * -, + *, - *, * *
for tehe1 in tehted:
    tulemus = 0
    for tehe2 in tehted:
        if tehe1 == "*":
            tulemus = teetehe(arv2, arv3, tehe1)
            tulemus = teetehe(tulemus, arv4, tehe2)
        elif tehe2 == "*":
            tulemus = teetehe(arv3, arv4, tehe2)
            tulemus = teetehe(tulemus, arv2, tehe1)
        else:
            tulemus = teetehe(arv2, arv3, tehe1)
            tulemus = teetehe(tulemus, arv4, tehe2)
        if tulemus == arv1:
            print(str(arv1)+"="+str(arv2)+tehe1+str(arv3)+tehe2+str(arv4))
            exit(1)
# vordusmärk 2  + +, + -, - +, - -, * +, * -, + *, - *, * *
for tehe1 in tehted:
    tulemus = 0
    for tehe2 in tehted:
        tulemus1 = teetehe(arv1, arv2, tehe1)
        tulemus2 = teetehe(arv3, arv4, tehe2)
        if tulemus1 == tulemus2:
            print(str(arv1)+tehe1+str(arv2)+"="+str(arv3)+tehe2+str(arv4))
            exit(1)
# vordusmärk 3 + +, + -, - +, - -, * +, * -, + *, - *, * *
for tehe1 in tehted:
    tulemus = 0
    for tehe2 in tehted:
        if tehe1 == "*":
            tulemus = teetehe(arv1, arv2, tehe1)
            tulemus = teetehe(tulemus, arv3, tehe2)
        elif tehe2 == "*":
            tulemus = teetehe(arv2, arv3, tehe2)
            tulemus = teetehe(tulemus, arv1, tehe1)
        else:
            tulemus = teetehe(arv1, arv2, tehe1)
            tulemus = teetehe(tulemus, arv3, tehe2)
        if tulemus == arv4:
            print(str(arv1)+tehe1+str(arv2)+tehe2+str(arv3)+"="+str(arv4))
            exit(1)
print("EI SAA")



