import sys

read = sys.stdin.readline

n, m, k = map(int, read().split())

result = 0

while n >= 2 and m >= 1 and n + m >= k + 3:
    # n + m >= k + 3은 다음 차례에 계산할 수 있는지
    n -= 2
    m -= 1
    result += 1

print(result)