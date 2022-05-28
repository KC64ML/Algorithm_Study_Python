t = int(input())

answer = []

for i in range(1, t + 1):
    n = int(input())
    data = []
    result = 0

    for _ in range(n):
        a, b = map(int, input().split())
        if data:
            for da, db in data:
                if (a < da and b > db) or (a > da and b < db):
                    result += 1
        data.append((a, b))

    answer.append("#{} {}".format(i, result))

print('\n'.join(answer))