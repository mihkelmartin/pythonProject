import sys
tul = 1;
N = int(sys.stdin.readline())
for i in range(2, N + 1):
    tul *= i
    tulstr = str(tul)
    while tulstr[-1] == "0":
        tulstr = tulstr[0:-1]
    tul = int(tulstr[-1*min(len(str(i))+2, len(tulstr)):])
print(str(tul)[-1])
