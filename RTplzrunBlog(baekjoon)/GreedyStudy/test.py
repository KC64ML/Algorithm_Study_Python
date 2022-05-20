import sys

read = sys.stdin.readline

n = int(read())

for i in range(1, 2 * n):
    if i <= n:
        print('*' * i)
    else:
        print('*' * (2 * n - i))
