import bisect
import sys
s = sys.stdin.readline().split()

N = int(s[0])
M = int(s[1])
autod = []
tulemus = []
for i in range(N):
    autod.append(int(sys.stdin.readline()))

for j in range(M):
    maksta = int(input())
    parimvahe = 9999999999999999
    parimhind = 0

    # Kuna indeks võib olla ka viimane + 1, siis tuleb min
    indeks = min(bisect.bisect_left(autod, maksta), len(autod)-1)
    parimvahe = abs(autod[indeks] - maksta)

    # Kui parim indeks on 0, siis - 1 annab -1, seega teeme max kus teine liige 0
    eelmisega_vahe = abs(autod[max(indeks - 1, 0)] - maksta)
    if eelmisega_vahe <= parimvahe:
        indeks = max(indeks - 1, 0);
    parimhind = autod[indeks]

#   for hind in autod:
#        vahe = abs(maksta - hind)
#        if vahe >= parimvahe:
#            break
#        if vahe < parimvahe:
#            parimvahe = vahe
#            parimhind = hind
    tulemus.append(str(parimhind))

print(" ".join(tulemus))



