import sys

read = sys.stdin.readline

s = int(read())


n = 1

while (n +1) * n <= s * 2:
    n += 1

print(n-1)
