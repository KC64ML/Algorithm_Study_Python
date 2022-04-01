import sys
from itertools import permutations

read = sys.stdin.readline

n = int(read())

arr = list(map(int, read().split()))

# 순열로 조합한다.
cases = list(permutations(arr))

result = 0

for card in cases:
    ans = 0
    for idx in range(n - 1):
        ans += abs(card[idx] - card[idx + 1])
    result = max(result, ans)

print(result)
