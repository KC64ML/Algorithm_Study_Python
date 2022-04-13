import sys

read = sys.stdin.readline

t = int(read())

n = int(read())
a = list(map(int, read().split()))
m = int(read())
b = list(map(int, read().split()))

cnt = 0

dist = dict()


for i in range(len(a)):
    for j in range(i+1, len(a)+1):
        dist[sum(a[i:j])] = dist.get(sum(a[i:j]), 0) + 1

for i in range(len(b)):
    for j in range(i+1, len(b)+1):
        cnt += dist.get(t-sum(b[i:j]), 0)

print(cnt)
