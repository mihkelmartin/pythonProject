t = "IGNORE HIM!"
s = input()
sa = []
for taht in s:
    if taht not in sa:
        sa.append(taht)
if len(sa) % 2 == 0:
    t = "CHAT WITH HER!"
print(t)