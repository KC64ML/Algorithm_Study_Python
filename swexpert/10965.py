t = int(input())


def prime(num):
    d = 2

    while d <= num:
        if num % d == 0:
            dist[d] = dist.get(d, 0) + 1
            in_key.add(d)
            num = num / d
        else:
            d += 1


answer = []
for i in range(1, t + 1):
    a = int(input())
    dist = dict()
    in_key = set()

    res = 1

    prime(a)

    for in_in_key in in_key:
        if dist[in_in_key] % 2:
            res *= in_in_key

    answer.append('#{} {}'.format(i, res))

print('\n'.join(answer))
