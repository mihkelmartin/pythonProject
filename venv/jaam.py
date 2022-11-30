import sys
jaam = [[[[False, False, False, False, False, False, False] for i in range(25)] for i in range(25)] for i in range(25)]
ukseasukoht = {}
ukseasukoht["X-"] = 0
ukseasukoht["X+"] = 1
ukseasukoht["Y-"] = 2
ukseasukoht["Y+"] = 3
ukseasukoht["Z-"] = 4
ukseasukoht["Z+"] = 5

N = int(sys.stdin.readline())
for i in range(N):
    rida = sys.stdin.readline().split()
    jaama_solm = jaam[int(rida[0]) - 1][int(rida[1]) - 1][int(rida[2]) - 1]
    jaama_solm[ukseasukoht[rida[3]]] = True
lekkijaStr = sys.stdin.readline().split()

print("Pusa")