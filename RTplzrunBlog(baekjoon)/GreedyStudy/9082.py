import sys

read = sys.stdin.readline

t = int(read())

for i in range(t):
    n = int(read())

    block = list(map(int, read().rstrip()))
    block2 = list(read().rstrip())
    answer = 0

    for j in range(n):
        if j == 0 and block[j] != 0 and block[j + 1] != 0:
            block[j] -= 1
            block[j + 1] -= 1
            answer += 1
        elif j == n - 1 and block[j] != 0 and block[j - 1] != 0:
            block[j] -= 1
            block[j - 1] -= 1
            answer += 1
        elif 1 <= j <= n - 2 and block[j - 1] != 0 and block[j] != 0 and block[j + 1] != 0:
            block[j] -= 1
            block[j - 1] -= 1
            block[j + 1] -= 1
            answer += 1
    print(answer)
