import sys

kodeerija = sys.stdin.readline().split()
arvaja = sys.stdin.readline().split()

punane = 0
for j in range(len(kodeerija)):
    if arvaja[j] == kodeerija[j]:
        punane += 1

valge = 0
for i in range(len(arvaja)):
    yleval = 0
    all = 0
    for j in range(len(kodeerija)):
        if arvaja[j] == arvaja[i] and j < i: all += 1
        if kodeerija[j] == arvaja[i] and arvaja[i] != kodeerija[i]: yleval += 1

    if yleval > all:
        valge += 1

print(str(punane) + " " + str(valge))


