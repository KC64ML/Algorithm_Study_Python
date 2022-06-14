import sys

read = sys.stdin.readline

n = int(read())

crain = list(map(int, read().split()))

m = int(read())

weight = list(map(int, read().split()))

crain.sort()
weight.sort()
answer = 0

if max(weight) > max(crain):
    print(-1)
else:
    up = 0
    answer = 0
    while up != m:
        answer += 1
        cr_idx = n - 1
        for i in range(m - 1, -1, -1):
            # 방문한 곳이라면 continue
            if weight[i] == 0:
                continue
            if cr_idx == -1:
                break
            if weight[i] <= crain[cr_idx]:
                cr_idx -= 1
                up += 1
                # 방문한 곳은 0으로 체크
                weight[i] = 0

    print(answer)


