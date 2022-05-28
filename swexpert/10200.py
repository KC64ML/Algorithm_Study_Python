t = int(input())

answer = []
for i in range(1, t + 1):
    n, a, b = map(int, input().split())
    res = ''
    if a + b > n:
        res = '#{} {} {}'.format(i, min(a, b), a + b - n)
    else:
        res = '#{} {} {}'.format(i, min(a, b), 0)

    answer.append(res)

print('\n'.join(answer))