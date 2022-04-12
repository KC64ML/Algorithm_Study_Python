import sys

read = sys.stdin.readline
n, s = map(int, read().split())

arr = list(map(int, read().split()))

dist = dict()
ans = 0


def leftSeq(idx, cur_sum):
    if idx == n//2:
        dist[cur_sum] = dist.get(cur_sum, 0) + 1
        return

    leftSeq(idx + 1, cur_sum)
    leftSeq(idx + 1, cur_sum + arr[idx])


def rightSeq(idx, cur_sum):
    global ans

    if idx == n:
        ans += dist.get(s - cur_sum, 0)
        return

    rightSeq(idx + 1, cur_sum)
    rightSeq(idx + 1, cur_sum + arr[idx])


leftSeq(0, 0)
rightSeq(n // 2, 0)

if not s:
    ans -= 1
print(ans)
