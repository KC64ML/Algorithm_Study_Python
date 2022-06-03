import sys

read = sys.stdin.readline

n = int(read())

alpha = [[0, False] for _ in range(10)]

for i in range(n):
    a = read().rstrip()
    m = 1
    alpha[ord(a[0]) - 65][1] = True
    for j in range(len(a) - 1, -1, -1):
        alpha[ord(a[j]) - 65][0] += m
        m *= 10

alpha.sort(reverse=True)

if alpha[9][1]:
    for i in range(8,-1,-1):
        if not alpha[i][1]:
            del alpha[i]
            break

answer = 0

for i in range(9):
    answer += alpha[i][0] * (9-i)

print(answer)
