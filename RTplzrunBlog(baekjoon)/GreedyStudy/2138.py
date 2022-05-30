# 첫 번째 스위치를 눌렸을 경우 1, 2번 바뀌고
# 2 ~ n-1까지 스위치를 눌렀을 때는 n - 1, n, n + 1
# n 스위치를 눌렀을 때는 n - 1, n

# 0번 -> 1번 -> 2번 -> 3번 ~ 이와 같이 영향을 준다.
# 그러므로, 확인할 때 0번 스위치가 켜져있거나 꺼져있을 때를 대상으로 각각 확인한다.

import sys

read = sys.stdin.readline

n = int(read())
a = list(map(int, read().rstrip()))
b = list(map(int, read().rstrip()))


def switchSwap(num):
    if num == 1:
        num = 0
    else:
        num = 1
    return num


def switch(bulb, cnt):
    if cnt:
        bulb[0] = switchSwap(bulb[0])
        bulb[1] = switchSwap(bulb[1])

    for i in range(1, len(bulb)):
        if bulb[i - 1] != b[i - 1]:
            cnt += 1
            bulb[i - 1] = switchSwap(bulb[i - 1])
            bulb[i] = switchSwap(bulb[i])

            if i != len(bulb)-1:
                bulb[i + 1] = switchSwap(bulb[i + 1])

    if bulb == b:
        return cnt
    else:
        return -1


result0 = switch(a[:], 0)
result1 = switch(a[:], 1)

if result0 != -1 and result1 != -1:
    print(min(result0, result1))
elif result0 == -1 and result1 != -1:
    print(result1)
elif result0 != -1 and result1 == -1:
    print(result0)
else:
    print(-1)