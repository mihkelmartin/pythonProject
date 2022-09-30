N = int(input())
myndidstr = input().split()
myndid = []
for s in myndidstr:
    myndid.append(int(s))
myndid.sort(reverse = True)
summa = 0
mitu = 0
vahesumma = 0
for mynt in myndid:
    summa = summa + int(mynt)
for mynt  in myndid:
    vahesumma = vahesumma + int(mynt)
    mitu += 1
    if vahesumma > summa / 2:
        break
print(str(mitu))