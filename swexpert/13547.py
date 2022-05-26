t = int(input())

for i in range(t):
    s = list(map(str, input().rstrip()))
    answer = ''
    if s.count('x') >= 8:
        answer = 'NO'
    else:
        answer = 'YES'

    print('#{} {}'.format(i+1, answer))

