import sys

read = sys.stdin.readline

n, k = map(int, read().split())

coin = []

for i in range(n):
    coin.append(int(read()))

coin.sort(reverse=True)

answer = 0

for in_coin in coin:
    if k >= in_coin:
        answer += k // in_coin
        k %= in_coin

    if k == 0:
        break

print(answer)