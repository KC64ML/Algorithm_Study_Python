import sys

read = sys.stdin.readline

a = list(read().rstrip())
b = list(read().rstrip())

idx = len(b) - 1
while len(b) > len(a):
    if b[idx] == 'A':
        del b[idx]
    else:
        b = b[idx-1::-1]
    idx -= 1

if a == b:
    print(1)
else:
    print(0)

