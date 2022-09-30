level = int(input())
labitud = [False] * (level+ 1)
x = input().split()
y = input().split()
t = "I become the guy."
for p in range(1, len(x)):
    labitud[int(x[p])] = True
for p in range(1, len(y)):
    labitud[int(y[p])] = True
for i in range(1, level + 1):
    if labitud[i] == False:
        t = "Oh, my keyboard!"
        break
print(t)

