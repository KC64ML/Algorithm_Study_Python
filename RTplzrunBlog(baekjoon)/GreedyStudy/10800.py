import sys

read = sys.stdin.readline

n = int(read())

d = {i: [] for i in range(n)}
answer = [0] * n
totalSum = 0
arrC = [0] * 200020
arrS = [0] * 2020


for i in range(n):
    c, s = map(int, read().split())

    d[i].append(s)
    d[i].append(c-1)

colorBall = list(d.items())

colorBall.sort(key=lambda x: (x[1]))

for i in range(n):
    idx, [weight, color] = colorBall[i]

    arrC[color] += weight
    arrS[weight] += weight
    totalSum += weight

    answer[idx] = totalSum - arrC[color] - arrS[weight] + weight

    if i != 0 and weight == colorBall[i-1][1][0] and color == colorBall[i-1][1][1]:
        answer[idx] = answer[colorBall[i-1][0]]

print('\n'.join(map(str, answer)))
