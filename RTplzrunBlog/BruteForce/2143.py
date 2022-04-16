import sys

read = sys.stdin.readline

t = int(read())

n = int(read())
a = list(map(int, read().split()))
m = int(read())
b = list(map(int, read().split()))

answer = 0

dist = dict()

for i in range(n):
    cur_sum = 0
    for j in range(i, n):
        cur_sum += a[j]
        dist[cur_sum] = dist.get(cur_sum, 0) + 1

for i in range(m):
    cur_sum = 0
    for j in range(i, m):
        cur_sum += b[j]
        answer += dist.get(t-cur_sum, 0)

print(answer)

