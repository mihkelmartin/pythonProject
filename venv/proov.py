a = input().split()
N = int(a[0])
A = int(a[1])
auto = ""
hind = -1
sobivus = -1
nouded = []
for i in range(N):
    nouded.append(input())
for i in range(A):
    nimi = input()
    autoandmed = input().split()
    vahehind = int(autoandmed[0])
    omadusi = int(autoandmed[1])
    vahesobivus = 0
    for j in range(omadusi):
        noue = input()
        if noue in nouded:
            vahesobivus += 1
    if vahesobivus > sobivus:
        auto = nimi
        hind = vahehind
        sobivus = vahesobivus
    elif vahesobivus == sobivus and vahehind < hind:
        auto = nimi
        hind = vahehind
print(auto)


