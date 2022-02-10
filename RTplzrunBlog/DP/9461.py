import sys

t = int(sys.stdin.readline())

p = [0] * 110

for idx in range(1, 110):
    if idx == 1 or idx == 2 or idx == 3:
        p[idx] = 1
    elif idx == 4 or idx == 5:
        p[idx] = 2
    else:
        p[idx] = p[idx - 5] + p[idx - 1]

while t > 0:
    n = int(sys.stdin.readline())
    print(p[n])
    t -= 1
