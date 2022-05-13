import sys

read = sys.stdin.readline

x, y, w, s = map(int, read().split())

answer = (x + y) * w

if not (x + y) % 2:
    answer = min(answer, max(x, y) * s)
else:
    answer = min(answer, (max(x, y) - 1) * s + w)

answer = min(answer, min(x, y) * s + (max(x, y) - min(x, y)) * w)


print(answer)
