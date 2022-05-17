import sys

read = sys.stdin.readline

n = int(read())

chain = list(map(int, read().split()))

chain.sort()

s = 0
answer = 0
for i in range(len(chain)):
    cnt = n - i - 1
    s += chain[i]

    if s >= cnt:
        answer = cnt
        break

print(answer)
