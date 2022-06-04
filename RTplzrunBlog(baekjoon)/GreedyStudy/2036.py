import sys

read = sys.stdin.readline

n = int(read())

positive = []
negative = []

answer = 0

for i in range(n):
    num = int(read())

    if num <= 0:
        negative.append(num)
    elif num == 1:
        answer += 1
    else:
        positive.append(num)

negative.sort()
positive.sort(reverse=True)


firstlen = len(negative)
secondlen = len(positive)
if len(negative) % 2:
    answer += negative[firstlen - 1]
    firstlen -= 1

if len(positive) % 2:
    answer += positive[secondlen - 1]
    secondlen -= 1

for i in range(0, firstlen, 2):
    answer += negative[i] * negative[i + 1]

for i in range(0, secondlen, 2):
    answer += positive[i] * positive[i + 1]

print(answer)
