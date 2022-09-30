#
import sys

kodeerija = sys.stdin.readline().split()
arvaja = sys.stdin.readline().split()
punane = 0
valge = 0
for i in range(len(arvaja)):
    if arvaja[i] == kodeerija[i]:
        punane += 1
        kodeerija[i] = "X"
        arvaja[i] = "X"
for i in range(len(arvaja)):
    if arvaja[i] == "X":
        continue
    for j in range(len(kodeerija)):
        if kodeerija[j] == "X":
            continue
        if arvaja[i] == kodeerija[j]:
            valge += 1
            kodeerija[j] = "X"
            break
print(str(punane) + " " + str(valge))


