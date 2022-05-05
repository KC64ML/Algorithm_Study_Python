import sys

read = sys.stdin.readline


K, N = map(int, read().split())
arr = [int(read()) for _ in range(K)]
start, end = 1, max(arr) #이분탐색 처음과 끝위치


_max = max(arr)

# 반드시 max에서 +1 값이어야 한다.
_max += 1

_min = 0 # 탐색 길이 최솟값
_mid = 0 # 탐색 길이 중간값

while _min < _max:

    # 범위 내에서 중간 길이를 구한다.
    _mid = (_max + _min) // 2

    count = 0

    # arr[idx] // 중간 길이로 잘라서 총 몇개가 만들어지는지를 구한다.
    for idx in range(len(arr)):
        count += (arr[idx] // _mid)

    if count < N:
        _max = _mid
    else:
        _min = _mid + 1


print(_min-1)