import sys

read = sys.stdin.readline

t = int(read())

m, n = map(int, read().split())

a_arr = []
b_arr = []

for _ in range(m):
    a_arr.append(int(read()))

for _ in range(n):
    b_arr.append(int(read()))

distA = dict()
distB = dict()

distA[0] = distB[0] = 1

# 먼저 a 피자 기준
for i in range(m):
    tmp = 0
    for j in range(m):
        tmp += a_arr[(i + j) % m]
        if tmp > t:
            break
        else:
            distA[tmp] = distA.get(tmp, 0) + 1

# 이제 b 피자 기준
for i in range(n):
    tmp = 0
    for j in range(n):
        tmp += b_arr[(i + j) % n]
        if tmp > t:
            break
        else:
            distB[tmp] = distB.get(tmp, 0) + 1
distA[sum(a_arr)] = distB[sum(b_arr)] = 1

answer = 0
for i in range(t + 1):
    answer += (distA.get(i, 0) * distB.get(t - i, 0))

print(answer)
