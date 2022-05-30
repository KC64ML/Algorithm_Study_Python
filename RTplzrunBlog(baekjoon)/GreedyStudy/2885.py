import sys

read = sys.stdin.readline

k = int(read())

# 우리는 k개 정사각형을 먹어야 남은 수업을 졸지 않고 버틸 수 있다.
# 막대 초콜릿 하나를 나누어야 한다.
# 정사각형이 D개 있는 막대는 D/2개 막대 두 조각으로 쪼개진다.
# ex) 적어도 K개 정사각형을 먹어야 남은 수업을 졸지 않고 버틸 수 있다. K : 6개
# 세로 : 1, 가로를 보고 판단한다.
# 현재 크기가 8인 정사각형으로 이루어져 있다. (1개로)
# 6개를 만들 수 없어, 8 // 2로 반을 나눈다.
# 4, 4일 때도 6개를 만들 수 없어 4 // 2, 4 // 2 쪼갠다.
# 2, 2, 2, 2 일 때는 6개를 만들 수 있어 종료한다.
# 8 -> 4, 4 -> 2, 2, 2, 2
# - 가장 작은 초콜릿의 크기 : 8
# - 2번 쪼개야 한다.


chocolate = 1

while chocolate < k:
    chocolate *= 2

cnt = 0
answer = chocolate

while chocolate > 1:
    # 8 -> 4 -> 2
    # 2 + 2 + 2 = 6
    if k % chocolate == 0:
        break
    else:
        chocolate //= 2
        cnt += 1

print(answer, cnt)
