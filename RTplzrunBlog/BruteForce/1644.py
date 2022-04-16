import sys

# INF = 4000010

read = sys.stdin.readline

n = int(read())

if n == 1:
    print(0)
    sys.exit()

decimal = []
decimalCheck = [False] * (n+1)


def decimalFun():
    for i in range(2, n+1):
        if not decimalCheck[i]:
            decimal.append(i)
            for j in range(i + i, n+1, i):
                decimalCheck[j] = True

# 소수
decimalFun()

start = 0
end = 0
permission = decimal[0]

cnt = 0

while True:
    if permission == n:
        cnt += 1

    if permission >= n:
        permission -= decimal[start]
        start += 1
    else:
        end += 1

        if end == len(decimal) or decimal[end] > n:
            break
        permission += decimal[end]

print(cnt)