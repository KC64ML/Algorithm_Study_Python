r, g, b = input().split()
r = int(r)
g = int(g)
b = int(b)
cnt = 0

for i in range(0, r):
    for j in range(0, g):
        for z in range(0, b):
            print("%d %d %d" % (i, j, z))
            cnt += 1

print(cnt)
