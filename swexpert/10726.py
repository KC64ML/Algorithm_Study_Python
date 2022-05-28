tc = int(input())
answer = list()
for i in range(1, tc+1):
    n, m = map(int, input().split())
    res = 'ON'
    for j in range(n):
        if not m % 2:
            res = 'OFF'
            break
        else:
            m //= 2

    answer.append('#{} {}'.format(i, res))

print('\n'.join(answer))
