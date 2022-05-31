import sys

read = sys.stdin.readline

n, m = map(int, read().split())

arr = []

for _ in range(n):
    weight, price = map(int, read().split())
    arr.append((price, weight))

arr.sort(key=lambda x: (x[0], -x[1]))

ans = sys.maxsize
same = 0
weight = 0

for i in range(n):

    weight += arr[i][1]

    if i > 0 and arr[i][0] == arr[i - 1][0]:
        same += arr[i][0]
    else:
        same = 0

    # 현재 고기의 양이, 은혜가 필요한 고기의 양보다 많을 경우
    if weight >= m:
        # 가격을 비교한 후, 업데이트 한다.
        ans = min(ans, arr[i][0] + same)

answer = (ans if ans != sys.maxsize else -1)
print(answer)
