import sys
riigid = {}
for i in range(int(sys.stdin.readline())):
    maanimi = sys.stdin.readline().strip()
    riigid[maanimi] = [maanimi,0,0,-9999999,0,0]
for i in range(int(sys.stdin.readline())):
    mang = sys.stdin.readline().strip().split()
    maad = mang[0].split("-")
    maa1 = maad[0]
    maa2 = maad[1]
    varavad = mang[1].split(":")
    maa1varavad = int(varavad[0])
    maa2varavad = int(varavad[1])
    maa1andmed = riigid[maa1]
    maa2andmed = riigid[maa2]
    if maa1andmed[3] == -9999999:
        maa1andmed[3] = 0
    if maa2andmed[3] == -9999999:
        maa2andmed[3] = 0
    if maa1varavad > maa2varavad:
        maa1andmed[1] += 3
        maa1andmed[2] += 1
    elif maa1varavad < maa2varavad:
        maa2andmed[1] += 3
        maa2andmed[2] += 1
    else:
        maa1andmed[1] += 1
        maa2andmed[1] += 1
    maa1andmed[3] += maa1varavad - maa2varavad
    maa2andmed[3] += maa2varavad - maa1varavad
    maa1andmed[4] += maa1varavad
    maa2andmed[4] += maa2varavad
    maa1andmed[5] += 1
    maa2andmed[5] += 1
tulemus = []
for riik in riigid:
    tulemus.append(riigid[riik])
tulemus = sorted(tulemus, key = lambda x: (-x[1], -x[2],-x[3],-x[4], x[5], x[0]))
for s in tulemus:
    print(s[0])



