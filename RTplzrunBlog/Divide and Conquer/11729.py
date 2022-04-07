import sys

read = sys.stdin.readline

n = int(read())

result = []


def hanoitab(num, f, b, t):
    if num == 1:
        result.append((f, t))
    else:
        hanoitab(num - 1, f, t, b)
        result.append((f, t))
        hanoitab(num - 1, b, f, t)


hanoitab(n, 1, 2, 3)

print(len(result))
for x, y in result:
    print(x, y)
