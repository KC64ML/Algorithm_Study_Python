import sys

read = sys.stdin.readline

n, s = map(int, read().split())

arr = list(map(int, read().split()))

start = 0
end = 0
permission = arr[0]

result = 100001


while True:

    if permission >= s:
        permission -= arr[start]
        result = min(result, end - start+1)
        start += 1
    else:
        end += 1
        if end == n:
            break
        permission += arr[end]


if result == 100001:
    print(0)
else:
    print(result)
