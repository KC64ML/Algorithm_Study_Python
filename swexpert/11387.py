t = int(input())

for i in range(1, t + 1):
    d, l, n = map(int, input().split())
    answer = 0
    for j in range(n):
        answer += d * (1 + j * (l / 100))

    print('#{} {}'.format(i, int(answer)))
