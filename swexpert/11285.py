import math

ans = []

for t in range(int(input())):
    N = int(input())
    tot = 0
    for n in range(N):
        x, y = map(int, input().split())
        r = math.ceil(math.sqrt(x * x + y * y) / 20)
        if r <= 0:
            tot += 10
        elif r <= 11:
            tot += 11 - r
    ans.append(f"#{t + 1} {tot}")

for x in ans:
    print(x)