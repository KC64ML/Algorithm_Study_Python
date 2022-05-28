import math

t = int(input())

answer = []

for i in range(1, t + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    avg = sum(arr) / len(arr)
    res = 0

    for j in arr:
        if j <= avg:
            res += 1

    answer.append('#{} {}'.format(i, res))

print('\n'.join(answer))

