tc = int(input())

for i in range(1, tc + 1):
    n = int(input())
    p = list(map(int, input().split()))

    answer = 0
    for j in range(1, n - 1):
        if p[j - 1] < p[j] < p[j + 1] or p[j - 1] > p[j] > p[j + 1]:
            answer += 1

    print('#{} {}'.format(i, answer))
