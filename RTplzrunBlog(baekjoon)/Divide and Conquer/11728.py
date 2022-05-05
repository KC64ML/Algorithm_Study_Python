import sys

read = sys.stdin.readline

n, m = map(int, read().split())

a = list(map(int, read().split()))
b = list(map(int, read().split()))

result = a + b
result.sort()

print(' '.join(map(str, result)))
