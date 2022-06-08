import sys

read = sys.stdin.readline

a, b = map(int, read().split())

answer = 0

while b > a:
    answer += 1

    if b % 10 == 1:
        b = b // 10
    elif b % 2 == 0:
        b = b // 2
    elif b % 2 == 1:
        answer = -1
        break

    if b < a:
        answer = -1
        break
    elif a == b:
        break

if answer == -1:
    print(answer)
else:
    print(answer+1)