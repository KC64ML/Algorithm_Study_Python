import sys


# 전구의 상태 바꿈
def switch_button(num):
    if num == 0:
        num = 1
    else:
        num = 0

    return num


# 전구 스위치
def switch(state, cnt):
    # 첫번째 전구 스위치를 눌렀을 때 첫번째 전구와 두번째 전구의 상태를 바꿔준다.
    if cnt == 1:
        state[0] = switch_button(state[0])
        state[1] = switch_button(state[1])
    # 반복문을 통해 전구의 상태를 확인한다.
    for i in range(1, n):
        # 스위치 이전에 전구의 상태와 바꿔야하는 전구의 상태를 비교
        if state[i - 1] != after[i - 1]:
            cnt += 1
            # 이전 전구와 스위치 전구의 상태를 바꾼다.
            state[i - 1] = switch_button(state[i - 1])
            state[i] = switch_button(state[i])

            # 스위치 이후에 전구가 있다면 이후 전구의 상태를 바꾼다.
            if i != n - 1:
                state[i + 1] = switch_button(state[i + 1])

    # 현재 전구의 상태와 바꿔야하는 전구의 상태가 같으면 멈춘다.
    if state == after:
        return cnt

    # 바꿔야하는 전구의 상태로 바꾸지 못하므로 -1 출력
    else:
        return -1


n = int(sys.stdin.readline())
now = list(map(int, sys.stdin.readline().rstrip("\n")))
after = list(map(int, sys.stdin.readline().rstrip("\n")))

res1 = switch(now[:], 0)  # 첫번째 전구 스위치를 안누르고 시작한 경우
res2 = switch(now[:], 1)  # 첫번째 전구 스위치를 누르고 시작한 경우

# 2가지 조건으로 했을 때 더 작은 횟수를 출력
if res1 >= 0 and res2 >= 0:
    print(min(res1, res2))

# 0보다 큰 횟수를 출력
elif res1 >= 0 and res2 < 0:
    print(res1)
elif res1 < 0 and res2 >= 0:
    print(res2)

# 둘다 0보다 작기때문에 -1 출력
else:
    print(-1)


# 참고 : https://fre2-dom.tistory.com/55