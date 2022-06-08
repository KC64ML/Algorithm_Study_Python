import sys

read = sys.stdin.readline

alpha = read().split('-')
arr = []
for in_alpha in alpha:
    a = in_alpha.split('+')
    cnt = 0
    for in_a in a:
        cnt += int(in_a)
    arr.append(cnt)
n = arr[0]

for i in range(1, len(arr)):
    n -= arr[i]

print(n)
