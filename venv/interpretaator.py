kasud = input()
malu = 100 * [0]
asukoht = 0
for s in kasud:
    if s == "<":
        asukoht = ((asukoht - 1) + 100) % 100
    if s == ">":
        asukoht = (asukoht + 1) % 100
    if s == "+":
        malu[asukoht] = (malu[asukoht] + 1) % 256
    if s == "-":
        malu[asukoht] = ((malu[asukoht] - 1) + 256) % 256
for i in malu:
    print(str(i), end=" ")