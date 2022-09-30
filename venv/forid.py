N = int(input())
for i in range(N):
    arv = int(input())
    arvud = input().split()
    if arv == 1:
        print("YES")
        continue

    arvudint = []
    for s in arvud:
        arvudint.append(int(s))

    if arv == 2:
        if arvudint[1] - arvudint[0] > 3:
            print("NO")
        else:
            print("YES")
        continue

    saab = True
    for j in range(1, arv - 1):
        if arvudint[j] - arvudint[j-1] - 1 + arvudint[j+1] - arvudint[j] - 1 > 2:
            saab = False
    if saab:
        print("YES")
    else:
        print("NO")

