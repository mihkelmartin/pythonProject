N = int(input())
for i in range(N):
    arv = int(input())
    arvud = input().split()
    vahe = 0
    for i in range(len(arvud) - 1):
        vahe += int(arvud[i+1]) - int(arvud[i]) - 1
        if vahe > 2:
            break
    if vahe > 2:
        tulemus = "NO"
    else:
        tulemus = "YES"
    print(tulemus)


