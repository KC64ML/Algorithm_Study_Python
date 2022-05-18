import sys

read = sys.stdin.readline

n = int(read())

d = {i: [] for i in range(n)}
previousICB = [0] * 200100  # i번째이면 i-1 까지 컬러 볼 합 저장 리스트
previousICB2 = [0] * 200100  # i번째이면 i-1 까지 컬러 볼 합 저장 리스트
answer = [0] * n
totalSum = 0

for i in range(n):
    c, s = map(int, read().split())

    d[i].append(c)
    d[i].append(s)

colorBall = list(d.items())

colorBall.sort(key=lambda x: (x[1][1]))
beforeColorBall = 0
for idx, in_colorBall in colorBall:
    if previousICB[in_colorBall[0]]:
        answer[idx] = totalSum - previousICB[in_colorBall[0]]
    else:
        answer[idx] = totalSum

    if beforeColorBall != in_colorBall[0] and previousICB2[in_colorBall[1]]:
        answer[idx] -= in_colorBall[1] * previousICB2[in_colorBall[1]]

    previousICB2[in_colorBall[1]] += 1
    totalSum += in_colorBall[1]
    previousICB[in_colorBall[0]] += in_colorBall[1]
    beforeColorBall = in_colorBall[0]

print('\n'.join(map(str, answer)))
