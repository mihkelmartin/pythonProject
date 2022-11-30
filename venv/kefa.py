import sys
sys.stdin.readline()
s = sys.stdin.readline().split()
parimpikkus = 0
jooksevpikkus = 0
eelmine = 0
for number in s:
    if eelmine <= int(number):
        jooksevpikkus += 1
    else:
        jooksevpikkus = 1
    eelmine = int(number)
    parimpikkus = max(parimpikkus, jooksevpikkus)
print(parimpikkus)
