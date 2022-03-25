import sys

read = sys.stdin.readline

n = int(read())

arr = []

minus_cnt = 0

for _ in range(n):
    d = int(read())
    arr.append(d)

    if d < 0: minus_cnt += 1

arr.sort()

result = 0
before = 0
cnt = 1
zero_check = False

check = False

for i in range(n - 1, -1, -1):
    # print("i : ", i, " arr : ", arr[i])
    # 양수일 때
    if arr[i] > 0:
        # 1에 도착할 시
        if arr[i] == 1:
            result += 1
            before = 0
        # cnt가 홀 수일 때
        elif cnt % 2:
            before = arr[i]
            result += before
        else:
            result += (before * arr[i])
            result -= before
            before = 0

        cnt += 1

        # print("result = ", result)
    # 0일 때
    elif arr[i] == 0:
        # 음수자리가 홀 수이면 0이 존재한다면 곱해줘야 한다.
        if minus_cnt % 2 != 0:
            zero_check = True
    else:
        if not check:
            check = True
            cnt = 0
            # print(zero_check, minus_cnt)
            # 만약 남은 음수들이 홀 수개라면
            if minus_cnt % 2 != 0:
                # 0이 존재한다면
                if zero_check:
                    result += 0 * arr[i]
                else:
                    result += arr[i]
            else:
                # 남은게 짝수라면
                cnt = 1
                before = arr[i]
        else:
            if cnt % 2:
                before = arr[i]
            else:
                result += (before * arr[i])
                before = 0
        cnt += 1
        # print("result = ", result)

print(result)
