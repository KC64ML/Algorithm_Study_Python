t = int(input())
answer = list()
for i in range(1, t+1):
    alpha = list(input().rstrip())
    alpha.sort()
    idx = 0
    res = list()

    while idx < len(alpha):

        if idx < len(alpha) - 1 and alpha[idx] == alpha[idx+1]:
            idx += 2
            continue
        else:
            res.append(alpha[idx])
            idx += 1

    if not res:
        res = 'Good'
    answer.append('#{} {}'.format(i, ''.join(res)))

print('\n'.join(answer))