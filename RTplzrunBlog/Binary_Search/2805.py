import sys

read = sys.stdin.readline

n, m = map(int, read().split())

arr = list(map(int, read().split()))

arr.sort()

sta = 0
end = len(arr)-1
total = 0

while sta < end:
    mid = (arr[sta] + arr[end]) // 2

    left_max = 0
    right_min = 0
    check = False
    result = 0

    for i in range(sta, end + 1):
        if mid < arr[i]:
            if not check:
                left_max = (i - 1)
                right_min = i

            result += arr[i] - mid

    if result == m:
        total = result
        break
    elif result < m:
        end = left_max
    else:
        sta = right_min

print(total)


# 참고 https://claude-u.tistory.com/446