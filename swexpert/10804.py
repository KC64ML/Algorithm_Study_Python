t = int(input())

answer = []

for i in range(1, t+1):
    mirror = list(input().rstrip())
    res = ''
    for j in range(len(mirror)):
        r = mirror[len(mirror) - j - 1]
        if r == 'b':
            r = 'd'
        elif r == 'd':
            r = 'b'
        elif r == 'p':
            r = 'q'
        else:
            r = 'p'
        res += r
    answer.append('#{} {}'.format(i, res))

print('\n'.join(answer))
