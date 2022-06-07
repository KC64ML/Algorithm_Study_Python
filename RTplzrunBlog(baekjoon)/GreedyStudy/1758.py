import sys

read = sys.stdin.readline

n = int(read())


tip = []

for i in range(n):
    tip.append(int(read()))

tip.sort(reverse=True)

answer = 0
for i in range(n):
    cur_t = tip[i] - (i + 1 - 1)
    if cur_t > 0:
        answer += tip[i] - (i + 1 - 1)
    else:
        answer += 0

print(answer)